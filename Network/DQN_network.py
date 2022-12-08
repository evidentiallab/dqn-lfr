import time
import pickle
import torch
import torch.nn as nn
import torch.nn.functional as F
# -*- coding: UTF-8 -*-

class Network(nn.Module):
    def __init__(self, input_dim, n_action):
        super(Network,self).__init__()
        self.f1 = nn.Linear(input_dim, 256)
        self.f2 = nn.Linear(256, 128)
        self.f3 = nn.Linear(128, 64)
        self.f4 = nn.Linear(64, n_action)
        self.device =torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.to(self.device)
        self.str_time = time.strftime("%Y%m%d%H%M%S")

    def forward(self, x):
        x = F.relu(self.f1(x))
        x = F.relu(self.f2(x))
        x = F.relu(self.f3(x))
        x = self.f4(x)
        return x

    def act(self, obs):
        state = obs.to(self.device)
        actions = self.forward(state)
        action = torch.argmax(actions).item()
        return action

    def save_net_pkl(self,path):
        with open(path,'wb') as model:
            pickle.dump(self,model)

    def load_net_pkl(self,load_path):
        with open(load_path,'rb') as model:
            load = pickle.load(model)
        return load
