from load_balancing_steiner_tree import *
from DQN.graph_generator1 import GraphGeneratorGrid2D

if __name__ == '__main__':
    path = '../Graph_and_Net_Model/22112632graph_model.pkl'
    # gm = GraphGeneratorGrid2D(5, 5, 2, 20)
    gm = GraphGeneratorGrid2D(5, 5, 2, 20).load_graph_model(load_path=path)
    # gm.generate_request(gm)
    # print(SimpleSteinerTree(gm).main(plot=True))
    # gm.save_graph_model()
    print(LoadBalancingSteinerTree(gm, 1).main(plot=True))
    # print(gm.src_node,gm.dst_node,gm.dst_list,gm.steiner_nodes)

