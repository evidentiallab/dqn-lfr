import torch
import time
import random
from tqdm import tqdm
import numpy as np
import networkx as nx
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import deque
from itertools import count
from matplotlib import pylab
import matplotlib.pyplot as plt
from Network.DQN_network import Network

import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

E_n = 2
_Bw = 20
net = 50
gamma = 0.98
size = 5000
terminal = 110
batch_size = 64
target_update_freq = 2
Train_list = [0.]
class Deeplearning:
    def __init__(self,graph_model):

        self.graph_model = graph_model
        self.m = self.graph_model.m
        self.n = self.graph_model.n
        self.G = self.graph_model.G
        self.pos = self.graph_model.pos
        self.str_time = self.graph_model.str_time
        self.directory = str('DQN/Graph_and_Net_Model/')+'model/'+self.str_time+ '_'+str(self.m)+str(self.n)\
                         +'/percent_'+str(self.graph_model.percentage)+'/'
        self.str_time = time.strftime("%Y%m%d%H%M%S")

        # self.device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
        self.device = torch.device('cpu')
        self.num_actions = len(self.G.nodes())
        self.policy = Network(self.num_actions * 2, self.num_actions).to(self.device)
        self.target = Network(self.num_actions * 2, self.num_actions).to(self.device)
        self.target.load_state_dict(self.policy.state_dict())
        self.optimizer = optim.Adam(self.policy.parameters(), lr=1e-3)
        self.len = len(self.G.nodes())

        self.src_node = None
        self.dst_node = None
        self.alpha = 1
        self.beta = 1
        self.episode_reward=0.0
        self.score  = 0.0
        self.mid_rw = 0.0
        self.reward = [0.]
        self.reward_buffer = [0.]
        self.enc_node = {}
        self.dec_node = {}
        self.min_replay_size = int(self.n*size)
        self.replay_buffer = deque(maxlen = self.min_replay_size)
        self.action_list = []

        for index, nodes in enumerate(self.G.nodes()):
            self.enc_node[nodes] = index
            self.dec_node[index] = nodes

    def nodes_link(self, current_node, new_node):
        if new_node in self.G[current_node]:   #TODO bw = 0 break route refused!
            a = self.G[current_node][new_node]['weight']
            b = self.G[current_node][new_node]['bw']
            if b == 0:  # reject the bw = 0 link
                return -200,False
            reward = self.alpha *(-a) +self.beta * (-1)*round(_Bw/b,2)# _Bw >= 20

            return reward, True
        reward = -200
        return reward, False

    def reward_function(self, current, action):
        current = self.dec_node[current]
        new_node = self.dec_node[action]
        _reward, link = self.nodes_link(current, new_node)
        return _reward, link

    def state_encode(self, current_node, end):
        return current_node + self.len * end

    def state_decode(self, state):
        current = state % self.len
        end = (state - current) / self.len
        return current, int(end)

    def reset_state(self):
        state = self.state_encode(self.enc_node[self.graph_model.src_node], self.enc_node[self.graph_model.dst_node])
        return state

    def one_step(self, state, action):
        done = False
        current_node, end = self.state_decode(state)
        new_state = self.state_encode(action, end)
        reward, link = self.reward_function(current_node, action)
        if not link:
            new_state = state
            return new_state, reward, False
        elif action == end:
            a = self.G[self.dec_node[current_node]][self.graph_model.dst_node]['weight']
            b = self.G[self.dec_node[current_node]][self.graph_model.dst_node]['bw']
            reward = terminal+(self.alpha *(-a) +self.beta * (-1)*round(_Bw/b,2))
            done = True
        return new_state, reward, done

    def state_to_vector(self,current_node, end_node):
        source_state_zeros = [0.] * self.len
        source_state_zeros[current_node] = 1
        end_state_zeros = [0.] * self.len
        end_state_zeros[end_node] = 1.
        vector = source_state_zeros + end_state_zeros
        return vector

    # return a list of list converted from state to vectors
    def list_of_vectors(self,new_obses_t):
        list_new_obses_t = new_obses_t.tolist()
        # convert to integer
        list_new_obss_t = [int(v) for v in list_new_obses_t]
        vector_list = []
        for state in list_new_obss_t:
            s, f = self.state_decode(state)
            vector = self.state_to_vector(s, f)
            vector_list.append(vector)

        return vector_list

    def random_choose_action(self,obs):
        current_node, end = self.state_decode(obs)
        _current_node = self.dec_node[current_node]
        self.action_list = list(self.G[_current_node])
        for i,nodes in enumerate(self.action_list):
            self.action_list[i] = self.enc_node[nodes]
        action = np.random.choice(self.action_list)
        return action

    def plot_reward(self,reward, i,filename,plot_name):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
        plt.rcParams['axes.unicode_minus'] =False   #
        plt.ticklabel_format(style='sci', scilimits=(0, 0))
        plt.tick_params(labelsize=13)
        plt.plot(reward)
        plt.xlabel('Episode/k',fontsize=15)
        plt.ylabel(plot_name,fontsize=15)
        plt.savefig(self.directory + filename + str(i) + '.svg')
        plt.savefig(self.directory + filename + str(i) + '.pdf')

        plt.close()

    def build_net(self):

        transitions = random.sample(self.replay_buffer, batch_size)
        obses = np.asarray([t[0] for t in transitions])
        actions = np.asarray([t[1] for t in transitions])
        rews = np.asarray([t[2] for t in transitions])
        dones = np.asarray([t[3] for t in transitions])
        new_obses = np.asarray([t[4] for t in transitions])

        obses_t = torch.as_tensor(obses, dtype=torch.float32).to(self.device)
        actions_t = torch.as_tensor(actions, dtype=torch.int64).to(self.device).unsqueeze(-1)
        rews_t = torch.as_tensor(rews, dtype=torch.float32).to(self.device)
        dones_t = torch.as_tensor(dones, dtype=torch.float32).to(self.device)
        new_obses_t = torch.as_tensor(new_obses, dtype=torch.float32).to(self.device)

        list_new_obses_t = torch.tensor(self.list_of_vectors(new_obses_t)).to(self.device)
        target_q_values = self.target(list_new_obses_t)  ##input 32 output 16

        max_target_q_values = target_q_values.max(dim=1, keepdim=False)[0]
        ##Q-target = ymaxQ(s,a)+reward_buffer
        targets = rews_t + gamma * (1 - dones_t) * max_target_q_values
        targets = targets.unsqueeze(-1)  ##add a dim

        list_obses_t = torch.tensor(self.list_of_vectors(obses_t)).to(self.device)
        q_values = self.policy(list_obses_t)
        action_q_values = torch.gather(input=q_values, dim=1, index=actions_t)

        loss = nn.functional.mse_loss(action_q_values, targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def get_epsilon(self,episodes,i):

        epsilon = np.exp(-i / (episodes / E_n))
        return epsilon

    def take_action(self,plot,net_path):
        import time
        DQN_time = 0
        if net_path:
            self.policy.load_state_dict(torch.load(net_path))
        observation = self.reset_state()
        node = self.graph_model.src_node
        DQN_path,ILP_path = [],[]
        DQN_path.append(self.graph_model.src_node)
        while node != self.graph_model.dst_node and len(DQN_path) < 20:
            source, end = self.state_decode(observation)
            v_obs = self.state_to_vector(source, end)
            t_obs = torch.tensor([v_obs])
            _t = time.time()
            action = self.policy.act(t_obs)
            DQN_time += (time.time() - _t)
            new_observation, rew, done = self.one_step(observation, action)
            transition = (observation, action, rew, done, new_observation)
            self.replay_buffer.append(transition)
            observation = new_observation
            self.episode_reward += rew
            node = self.dec_node[action]
            DQN_path.append(node)

        ILP_path = self.graph_model.get_shortest_path(self.graph_model.src_node,self.graph_model.dst_node)
        if plot == True:
            self.plot_path(self.directory,DQN_path,'DQN_Result.')
            self.plot_path(self.directory,ILP_path,'ILP_Result')
        return DQN_path,ILP_path,self.episode_reward,DQN_time

    def plot_path(self, d,shortestpath, file_name):
        path_edge = []
        b = len(shortestpath) - 1
        for k in range(b):
            path_edge.append((shortestpath[k], shortestpath[k + 1]))
        plt.figure(num=None, figsize=(self.m * 2.65, self.n * 2.65), dpi=1200)
        plt.axis('off')

        edge_weight_bw = dict([((u, v,), str((int(d['weight']), int(d['bw']))))
                               for u, v, d in self.G.edges(data=True)])
        nx.draw(self.G, self.pos, with_labels=True)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=path_edge, edge_color='r', width=6.0)
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_weight_bw, font_size=15)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=self.G.nodes(), node_color='orange', node_size=800)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[self.graph_model.src_node], node_color='springgreen', node_size=800)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[self.graph_model.dst_node], node_color='red', node_size=800)

        cut = 1.00
        xmax = cut * max(xx for xx, yy in self.pos.values())
        ymax = cut * max(yy for xx, yy in self.pos.values())
        plt.xlim(-1, xmax + 1)
        plt.ylim(-1, ymax + 1)
        plt.savefig(d + file_name, bbox_inches="tight")
        pylab.close()

    def train(self, save_step, episodes):
        for _episodes in tqdm(range(episodes)):
            self.graph_model.generate_request(self.graph_model)
            obs = self.reset_state()
            for i in count():
                self.epsilon = self.get_epsilon(episodes,_episodes)
                rnd_sample = random.random()
                if rnd_sample < self.epsilon:
                    action = self.random_choose_action(obs)
                else:
                    source, end = self.state_decode(obs)   # source is the current node
                    v_obs = self.state_to_vector(source, end)
                    t_obs = torch.tensor([v_obs])
                    action = self.policy.act(t_obs)

                new_obs, rew, done = self.one_step(obs, action)
                transition = (obs, action, rew, done, new_obs)
                self.replay_buffer.append(transition)
                obs = new_obs
                self.episode_reward += rew

                if done:
                    self.episode_reward = round(self.episode_reward,2)
                    self.reward_buffer.append(self.episode_reward)
                    self.score += self.episode_reward
                    self.reward.append(self.score)
                    self.episode_reward = 0.
                    _episodes += 1
                    break
                if _episodes % net == 0 and _episodes > batch_size:
                    self.build_net()

            if _episodes % target_update_freq == 0:      # load the data from policy to target
                self.target.load_state_dict(self.policy.state_dict())
            if _episodes % save_step == 0 :
                if not os.path.exists(self.directory):
                    os.mkdir(self.directory)
                torch.save(self.policy.state_dict(),self.directory+'/policy_net-'+str(_episodes)+'.pth')
            if _episodes % (save_step*100) == 0:
                print('\n',self.reward_buffer[-20:-1],'\n')
                print('step', _episodes, 'self.epsilon:', round(self.epsilon,2),
                      'A_R', np.round(np.mean(self.reward_buffer), 2))
            # Train_list.append(_episodes/1000)
        self.plot_reward(self.reward, episodes, "Score", "Cumulative")
        self.plot_reward(self.reward_buffer, episodes, "Reward", "Single-step")
