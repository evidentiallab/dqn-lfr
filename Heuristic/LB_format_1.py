import matplotlib.pyplot as plt

c = 0
w = []
b = []
if c:
    for i in range(1,21,2):
        y = []
        w.append(i)
        for j in range(1,21,2):
            y.append(round(i+j,2))
        b.append(y)
    print(w)
    print(b)
    plt.title('Metric')  # 折线图标题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('bandwidth')  # x轴标题 bandwidth
    plt.ylabel('Loadbalancing')  # y轴标题 LB
    plt.plot(w, b[1], marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(w, b[2], marker='o', markersize=3)
    plt.plot(w, b[3], marker='o', markersize=3)
    plt.plot(w, b[4], marker='o', markersize=3)
    plt.plot(w, b[5], marker='o', markersize=3)

    plt.legend(['weight=3', 'weight=5', 'weight=7', 'weight=9', 'weight=11'])  # 设置折线名称
    plt.show()

if 1-c:
    for i in range(1,21,2):
        y = []
        w.append(i)
        for j in range(1,21,2):
            y.append(round(j+i,2))
        b.append(y)
    print(w)
    print(b)
    plt.title('Metric')  # 折线图标题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('weight')  # x轴标题
    plt.ylabel('LB')  # y轴标题
    plt.plot(w, b[1], marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(w, b[2], marker='o', markersize=3)
    plt.plot(w, b[3], marker='o', markersize=3)
    plt.plot(w, b[4], marker='o', markersize=3)
    plt.plot(w, b[5], marker='o', markersize=3)
    plt.plot(w, b[6], marker='o', markersize=3)

    plt.legend([ 'bandwidth=3', 'bandwidth=5', 'bandwidth=7', 'bandwidth=9', 'bandwidth=11','bandwidth=13'])  # 设置折线名称
    plt.show()
    # if Test:
    #     t_1 = t_2 = t_3 = t_4 = 0
    #     count_Heu = count_DQN = count_DQN_Heu = 0
    #     for i in range(Test_total):
    #         Graph_model.generate_request(Graph_model)
    #         p1,t1 = ILP_solution()          # load balancing  beta*(max-min)
    #         p2,t2 = Dijkstra_solution()     # shortest path with weight
    #         p3,t3 = Heuristic_solution()    # LB_1 = a*W+b*(k/B)
    #         p4,t4 = DQN_solution(test_one=True)
    #         p1.sort()
    #         p2.sort()
    #         p3.sort()
    #         p4.sort()
    #         if p2 == p3:
    #             count_Heu += 1
    #         if p2 == p4:
    #             count_DQN += 1
    #         if p3 == p4:
    #             count_DQN_Heu += 1
    #         t_1 += t1
    #         t_2 += t2
    #         t_3 += t3
    #         t_4 += t4
    #         print(round(t_1,5),round(t_2,5),round(t_3,5),round(t_4,5))
    #     print("Heu:", round(count_Heu / Test_total, 3),"DQN_1:",round(count_DQN / Test_total, 3),
    #           "DQN_Heu:",round(count_DQN_Heu / Test_total, 3))