from ILP.load_balancing_steiner_tree import LoadBalancingSteinerTree
from ILP.Graph_generator import GraphGeneratorGrid2D
from DQN.Grid2D_dqn_train import Deeplearning
from Heuristic.k_shortest_path import k_shortest_paths

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time

Generate = 0
Train = 0
Test = 1
Test_one = 0
Graph_m = 5
Graph_n = Graph_m
percentage = 1
Network_pth = 100
Train_episodes = 50001
Test_total = 200
train_episodes = 0
str_time = time.strftime("%y""%m""%d""%S")

w = 490
h = 499
axes_t =(0.3, 0.15, 0.8, 0.7)
axes_w =(0.3, 0.3, 1.2, 1.2)

def ILP_solution(model):                ## 1.ILP
    ILP_path = []
    weight_ILP = 0
    cost, res,time = LoadBalancingSteinerTree(model, 10).main(plot=False)
    for i in res:
        weight_ILP += model.int_link_dict[i].weight
        if model.int_link_dict[i].node_1 not in ILP_path:
            ILP_path.append(model.int_link_dict[i].node_1)
        if model.int_link_dict[i].node_2 not in ILP_path:
            ILP_path.append(model.int_link_dict[i].node_2)
    # print("ILP:", ILP_path, '\n', "ILP_time:", "cost:",cost, "time:", time, '\n')
    return ILP_path,weight_ILP,time,res

def Dijkstra_solution(model):            ## 2.Dijkstra
    weight_GIJ = 0
    Dj_pre = time.time()
    p = nx.shortest_path(G, model.src_node, model.dst_node, weight='weight')
    Dj_after = time.time()-Dj_pre
    for i in range(len(p)-1):
        weight_GIJ += model.n1n2_link_dict[(p[i],p[i+1])].weight
    # print("Dijkstra:", p, '\n', "time:", Dj_after - Dj_pre)
    return p,weight_GIJ,Dj_after

def Heuristic_solution(model):             ## 3.Heuristic
    weight_Heu =0
    Heuristic_pre = time.time()
    length, path = k_shortest_paths(G_contrast_Positive, model.src_node, model.dst_node,  3)
    Heuristic_after = time.time()-Heuristic_pre
    p =path[0]
    for i in range(len(p)-1):
        weight_Heu += model.n1n2_link_dict[(p[i],p[i+1])].weight
    # print("Heuristic:", path, '\n', "cost:",length, "time:", Heuristic_after - Heuristic_pre)
    return p,weight_Heu,Heuristic_after

def DQN_solution(model,path=None,Generate= False,Train = False,test_one = False):
    weight_DQN = 0
    if Generate:
        """generate model"""
        model = GraphGeneratorGrid2D(Graph_m, Graph_n, percentage)
        model.save_graph_model()
        # print the ILP result simple and balancing
        model.draw_and_save("generator.png")
    if Train:
        """Load graph model and Training"""
        DQN_model.train(Network_pth, Train_episodes)
    if test_one:
        DQN_path, ILP_path, reward,_t = DQN_model.take_action(plot=False, net_path=path)
        for i in range(len(DQN_path) - 1):
            try:
                weight_DQN += model.n1n2_link_dict[DQN_path[i], DQN_path[i + 1]].weight
            except KeyError:
                weight_DQN += 200
        return DQN_path,weight_DQN, _t

def zone_and_linked(ax, axins, zone_left, zone_right, x, y, linked,
                    x_ratio=0.02, y_ratio=0.02):
    """缩放内嵌图形，并且进行连线
    ax:         调用plt.subplots返回的画布。例如： fig,ax = plt.subplots(1,1)
    axins:      内嵌图的画布。 例如 axins = ax.inset_axes((0.4,0.1,0.4,0.3))
    zone_left:  要放大区域的横坐标左端点
    zone_right: 要放大区域的横坐标右端点
    x:          X轴标签
    y:          列表，所有y值
    linked:     进行连线的位置，{'bottom','top','left','right'}
    x_ratio:    X轴缩放比例
    y_ratio:    Y轴缩放比例
    """
    xlim_left = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
    xlim_right = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio

    y_data = np.hstack([yi[zone_left:zone_right] for yi in y])
    ylim_bottom = np.min(y_data) - (np.max(y_data) - np.min(y_data)) * y_ratio
    ylim_top = np.max(y_data) + (np.max(y_data) - np.min(y_data)) * y_ratio
    axins.set_xlim(xlim_left, xlim_right)
    axins.set_ylim(ylim_bottom, ylim_top)

    ax.plot([xlim_left, xlim_right, xlim_right, xlim_left, xlim_left],
            [ylim_bottom, ylim_bottom, ylim_top, ylim_top, ylim_bottom], "black")

    if linked == 'bottom':
        xyA_1, xyB_1 = (xlim_left, ylim_top), (xlim_left, ylim_bottom)
        xyA_2, xyB_2 = (xlim_right, ylim_top), (xlim_right, ylim_bottom)
    elif linked == 'top':
        xyA_1, xyB_1 = (xlim_left, ylim_bottom), (xlim_left, ylim_top)
        xyA_2, xyB_2 = (xlim_right, ylim_bottom), (xlim_right, ylim_top)
    elif linked == 'left':
        xyA_1, xyB_1 = (xlim_right, ylim_top), (xlim_left, ylim_top)
        xyA_2, xyB_2 = (xlim_right, ylim_bottom), (xlim_left, ylim_bottom)
    elif linked == 'right':
        xyA_1, xyB_1 = (xlim_left, ylim_top), (xlim_right, ylim_top)
        xyA_2, xyB_2 = (xlim_left, ylim_bottom), (xlim_right, ylim_bottom)

    con = ConnectionPatch(xyA=xyA_1, xyB=xyB_1, coordsA="data",
                          coordsB="data", axesA=axins, axesB=ax)
    axins.add_artist(con)
    con = ConnectionPatch(xyA=xyA_2, xyB=xyB_2, coordsA="data",
                          coordsB="data", axesA=axins, axesB=ax)
    axins.add_artist(con)
def plot_svg(x,y,w,h,axes,y_name,file_name,signal):

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y[0], label='Heuristic', alpha=0.7, marker='o', markersize=3)
    ax.plot(x, y[1], label='DQN_1', alpha=0.7, marker='v', markersize=3)
    ax.plot(x, y[2], label='ILP', alpha=0.7, marker='x', markersize=3)
    ax.legend(loc='best',fontsize=13)
    ax.set_xlabel(xlabel='回合/k',fontsize=15)
    ax.set_ylabel(ylabel=y_name,fontsize=15)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    axins = inset_axes(ax, width="40%", height="30%", loc='lower left',
                       bbox_to_anchor=axes,
                       bbox_transform=ax.transAxes)  # （x0,y0,width,height）
    zone_and_linked(ax, axins, w, h, x, y[:2], 'top')

    axins.plot(x, y[0], label='Heuristic', alpha=0.7, marker='o', markersize=4)
    axins.plot(x, y[1], label='DQN_1', alpha=0.7, marker='v', markersize=4)
    if signal:
        axins.plot(x, y[2], label='ILP', alpha=0.7, marker='x', markersize=4)
    fig.savefig(file_name, dpi=1200)
    plt.close()

if __name__ == '__main__':
    graph_path = 'DQN/Graph_and_Net_Model/model/22120736_55/graph_model.pkl'
    Graph_model = GraphGeneratorGrid2D(Graph_m, Graph_n, percentage).load_graph_model(graph_path)
    DQN_model = Deeplearning(Graph_model)
    G = Graph_model.G
    G_contrast_Positive = Graph_model.G_contrast_Positive
    G_contrast_Inverse = Graph_model.G_contrast_Inverse
    directory  = Graph_model.directory
    graph_save_path = str('DQN/Graph_and_Net_Model/')+'model/'+str_time+\
                             '_'+str(Graph_m)+str(Graph_m)+'/'
    if Generate:
        DQN_solution(Graph_model,Generate=True)
    if Train:
        DQN_solution(Graph_model,Train=True)
    if Test_one:
        Graph_model.generate_request(Graph_model)
        net_path = "DQN/Graph_and_Net_Model/model/22120736_55/percent_1/policy_net-45000.pth"
        p1, w1, t1,res = ILP_solution(Graph_model)      # load balancing  beta*(max-min)
        p2, w2, t2 = Dijkstra_solution(Graph_model)     # shortest path with weight
        p3, w3, t3 = Heuristic_solution(Graph_model)    # LB_1 = a*W+b*(k/B)
        p4, w4, t4 = DQN_solution(Graph_model,path=net_path, test_one=True)
        Graph_model.draw_and_save_load_balancing_steiner_tree(res,directory+'ILP.pdf')
        DQN_model.plot_path(directory,p3, 'Heuristic.pdf')
        DQN_model.plot_path(directory,p4, 'DQN_1.pdf')
        print('w1:',w1,'w3:',w3,'w4:',w4)
    if Test:
        right_list_ILP, time_list_ILP = [], []
        right_list_Heu, time_list_Heu = [], []
        right_list_DQN, time_list_DQN = [], []
        weight_list_ILP, weight_list_Dij, weight_list_Heu, weight_list_DQN = [],[],[],[]
        Train_list = []
        for train_episodes in range(Network_pth, Train_episodes, Network_pth):
            net_path = 'DQN/Graph_and_Net_Model/model/22120736_55/percent_1/policy_net-' + str(train_episodes) + '.pth'
            Train_list.append(train_episodes/1000)
            t_1 = t_2 = t_3 = t_4 = 0
            w_1 = w_2 = w_3 = w_4 = 0
            count_Heu = count_DQN = count_DQN_Heu = 0
            for i in range(Test_total):
                Graph_model.generate_request(Graph_model)
                p1,w1,t1,res = ILP_solution(Graph_model)      # load balancing  beta*(max-min)
                p2,w2,t2 = Dijkstra_solution(Graph_model)     # shortest path with weight
                p3,w3,t3 = Heuristic_solution(Graph_model)    # LB_1 = a*W+b*(k/B)
                p4,w4,t4 = DQN_solution(Graph_model,path=net_path,test_one=True)
                p1.sort()
                p2.sort()
                p3.sort()
                p4.sort()
                if p1 == p3:
                    count_Heu += 1
                if p1 == p4:
                    count_DQN += 1
                if p3 == p4:
                    count_DQN_Heu += 1
                t_1 += t1
                t_2 += t2
                t_3 += t3
                t_4 += t4
                w_1 += w1
                w_2 += w2
                w_3 += w3
                w_4 += w4
            weight_list_ILP.append(round(w_1/Test_total,2))
            # weight_list_Dij.append(round(w_2/Test_total,2))
            weight_list_Heu.append(round(w_3/Test_total,2))
            weight_list_DQN.append(round(w_4/Test_total,2))
            right_list_Heu.append(100*round(count_Heu / Test_total, 2))
            right_list_DQN.append(100*round(count_DQN / Test_total, 2))
            time_list_ILP.append(1000*round(t_1,2))
            time_list_Heu.append(1000*round(t_3,2))
            time_list_DQN.append(1000*round(t_4,2))

        y_t = [time_list_Heu,time_list_DQN,time_list_ILP]
        y_w = [weight_list_Heu,weight_list_DQN,weight_list_ILP]
        plot_svg(Train_list, y_t, w, h, axes_t,'时间/ms', "Time.svg", 0)
        plot_svg(Train_list, y_t, w, h, axes_t,'时间/ms', "Time.pdf", 0)
        plot_svg(Train_list, y_w, w, h, axes_w,'成本', "weight.svg", 1)
        plot_svg(Train_list, y_w, w, h, axes_w,'成本', "weight.pdf", 1)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
        plt.xlabel('回合/k',fontsize=15)  # x轴标题 bandwidth
        plt.ylabel('相似度/%',fontsize=15)  # y轴标题 LB
        plt.ylim(0, 100)
        plt.plot(Train_list, right_list_Heu, marker='o', markersize=4)  # 绘制折线图，添加数据点，设置点的大小
        plt.plot(Train_list, right_list_DQN, marker='v', markersize=4)
        plt.legend(['Heuristic', 'DQN_1'],fontsize=13)  # 设置折线名称
        plt.savefig("Right_Rate.svg", dpi=1200)
        plt.savefig("Right_Rate.pdf", dpi=1200)

        plt.close()
