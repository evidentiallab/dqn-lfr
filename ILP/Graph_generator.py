from __future__ import print_function
import time
import pickle
import random
import networkx as nx
from ILP.link import Link
from random import randint
from matplotlib import pylab
import matplotlib.pyplot as plt
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

alpha = 1
beta = 1

class GraphGeneratorGrid2D(object):
    def __init__(self, m, n,percentage):
        """generating"""
        self.m = m
        self.n = n
        self.percentage = percentage
        self.G = nx.grid_2d_graph(m, n)
        self.G_contrast_Positive = nx.grid_2d_graph(m, n)
        self.G_contrast_Inverse = nx.grid_2d_graph(m, n)
        self.pos = dict(zip(self.G, self.G))
        Z = random.sample(list(self.G.nodes()), 2)
        self.src_node = Z[0]
        self.dst_list = Z[1:]
        self.dst_node = Z[1]
        self.steiner_nodes = Z[:]
        self.str_time = time.strftime("%y""%m""%d""%S")
        self.time = self.str_time
        self.directory = str('DQN/Graph_and_Net_Model/')+'model/'+self.str_time+ \
                         '_'+str(self.m)+str(self.n)+'/'
        self.save_graph_path = self.directory + 'graph_model.pkl'
        self.int_node_dict = {}
        self.node_int_dict = {}
        count = 0
        for i in range(m):
            for j in range(n):
                self.int_node_dict[count] = (i, j)
                self.node_int_dict[(i, j)] = count
                count += 1
        self.number_nodes = count

        self.int_link_dict = {}
        self.n1n2_link_dict = {}
        es = self.G.edges() ###
        count = 0
        for e in es:
            weight = randint(1,20)
            bandwidth = self.generate_bw()
            link = Link(count, e[0], e[1], weight, bandwidth)
            self.G.add_edge(e[0], e[1], weight=link.weight, bw=link.bw)
            weight_contrast_Positive = alpha*(link.weight)+beta*(20-link.bw)
            weight_contrast_Inverse = alpha*(link.weight)+beta*(round(20/link.bw,2))
            self.G_contrast_Positive.add_edge(e[0], e[1], weight=weight_contrast_Positive)
            self.G_contrast_Inverse.add_edge(e[0], e[1], weight=weight_contrast_Inverse)
            self.int_link_dict[count] = link
            self.n1n2_link_dict[(e[0], e[1])] = link
            self.n1n2_link_dict[(e[1], e[0])] = link
            count += 1
        self.number_links = count

    def generate_bw(self):
        # bandwidth = int((randint(1,20)*self.percentage)//1)
        # return bandwidth if bandwidth > 1 else 0
        bandwidth = randint(1,20)
        return bandwidth

    def get_link_weight_int(self, i):
        return self.int_link_dict[i].weight

    def get_link_bw_int(self, i):
        return self.int_link_dict[i].bw

    def get_shortest_path(self, src, dst):
        p = nx.shortest_path(self.G_contrast_Positive, src, dst,weight='weight')
        return p

    def generate_request(self,graph_model):
        _list = random.sample(list(self.G.nodes()),2)
        graph_model.src_node = _list[0]
        graph_model.dst_node = _list[1]
        graph_model.dst_list = [_list[1]]
        graph_model.steiner_nodes = _list[:]
        self.save_graph_model()#

    def draw_and_save_shortest_path(self, shortest_path, file_name, src, dst):
        path_edges = []
        for i in range(len(shortest_path)-1):
            path_edges.append((shortest_path[i],shortest_path[i+1]))
        plt.figure(num=None, figsize=(self.m * 2, self.n * 2), dpi=80)
        plt.axis('off')
        # https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.edges.html
        edge_weight_bw = dict([((u, v,), str((int(d['weight']), int(d['bw'])))) for u, v, d in self.G.edges(data=True)]) ###
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_weight_bw)
        nx.draw(self.G, self.pos, with_labels=True)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=path_edges,
                               edge_color='r',
                               width=8.0)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=self.G.nodes(), node_color='orange')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[src], node_color='green')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[dst], node_color='red')

        cut = 1.00
        xmax = cut * max(xx for xx, yy in self.pos.values())
        ymax = cut * max(yy for xx, yy in self.pos.values())
        plt.xlim(-1, xmax + 1)
        plt.ylim(-1, ymax + 1)

        plt.savefig(self.directory +file_name, bbox_inches="tight", dpi=200)
        pylab.close()
    def draw_and_save_load_balancing(self, balancing_path, file_name, src, dst):

        plt.figure(num=None, figsize=(self.m * 2, self.n * 2), dpi=80)
        plt.axis('off')
        # https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.edges.html
        edge_weight_bw = dict([((u, v,), str((int(d['weight']), int(d['bw'])))) for u, v, d in self.G.edges(data=True)]) ###
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_weight_bw)
        nx.draw(self.G, self.pos, with_labels=True)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=balancing_path,
                               edge_color='r',
                               width=8.0)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=self.G.nodes(), node_color='orange')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[src], node_color='green')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[dst], node_color='red')

        cut = 1.00
        xmax = cut * max(xx for xx, yy in self.pos.values())
        ymax = cut * max(yy for xx, yy in self.pos.values())
        plt.xlim(-1, xmax + 1)
        plt.ylim(-1, ymax + 1)

        plt.savefig(self.directory +file_name, bbox_inches="tight", dpi=200)
        pylab.close()

    def draw_and_save_simple_steiner_tree(self, steiner_links_int, file_name_draw,src,dst):
        steiner_edges = []
        for i in steiner_links_int:
            steiner_edges.append((self.int_link_dict[i].node_1, self.int_link_dict[i].node_2))
        plt.figure(num=None, figsize=(self.m * 2, self.n * 2), dpi=80)
        plt.axis('off')
        # https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.edges.html
        edge_weight_bw = dict([((u, v,), int(d['weight'])) for u, v, d in self.G.edges(data=True)]) ###
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_weight_bw)
        nx.draw(self.G, self.pos, with_labels=True)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=steiner_edges,
                               edge_color='r',
                               width=5.0)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=self.G.nodes(), node_color='orange') ###
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[src], node_color='blue')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[dst], node_color='green') ###

        cut = 1.00
        xmax = cut * max(xx for xx, yy in self.pos.values())
        ymax = cut * max(yy for xx, yy in self.pos.values())
        plt.xlim(-1, xmax + 1)
        plt.ylim(-1, ymax + 1)

        plt.savefig(self.directory+file_name_draw, bbox_inches="tight", dpi=200)
        pylab.close()

    def draw_and_save_load_balancing_steiner_tree(self, steiner_links_int, file_name_draw):
        steiner_edges = []
        for i in steiner_links_int:
            steiner_edges.append((self.int_link_dict[i].node_1, self.int_link_dict[i].node_2))
        plt.figure(num=None, figsize=(self.m * 2.65, self.n * 2.65), dpi=200)
        plt.axis('off')
        # https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.edges.html
        edge_weight_bw = dict([((u, v,), str((int(d['weight']), int(d['bw'])))) for u, v, d in self.G.edges(data=True)]) ###
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_weight_bw, font_size=15)
        nx.draw(self.G, self.pos, with_labels=True)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=steiner_edges,
                               edge_color='r',
                               width=6.0)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=self.G.nodes(), node_color='orange')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[self.src_node], node_color='springgreen')
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[self.dst_node], node_color='red')

        cut = 1.00
        xmax = cut * max(xx for xx, yy in self.pos.values())
        ymax = cut * max(yy for xx, yy in self.pos.values())
        plt.xlim(-1, xmax + 1)
        plt.ylim(-1, ymax + 1)

        plt.savefig(file_name_draw, bbox_inches="tight")
        pylab.close()

    def save_graph_model(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        with open(self.save_graph_path,'wb') as model:
            pickle.dump(self, model)

    def load_graph_model(self,load_path):
        with open(load_path,'rb') as model:
            load = pickle.load(model)
            model.close()
        return load

    def draw_and_save(self, file_name_draw):
        p = self.get_shortest_path(self.src_node,self.dst_node)
        self.draw_and_save_shortest_path(p, file_name_draw,self.src_node,self.dst_node)


if __name__ == '__main__':

    gm = GraphGeneratorGrid2D(5, 5, 1)
    gm.save_graph_model()
    gm.draw_and_save("generator.pdf")