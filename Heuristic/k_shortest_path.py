# -*- coding: utf-8 -*-
from heapq import heappush, heappop
from itertools import count
import networkx as nx

def k_shortest_paths(G, source, target, k=1, weight='weight'):
    """Returns the k-shortest paths from source to target in a weighted graph G.
    Parameters
    ----------
    G : NetworkX graph
    source : node
       Starting node
    target : node
       Ending node

    k : integer, optional (default=1)
        The number of shortest paths to find
    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight
    Returns
    -------
    lengths, paths : lists
       Returns a tuple with two lists.
       The first list stores the length of each k-shortest path.
       The second list stores each k-shortest path.
    Raises
    ------
    NetworkXNoPath
       If no path exists between source and target.
    Examples
    --------
    # >>> G=nx.complete_graph(5)
    # >>> print(k_shortest_paths(G, 0, 4, 4))
    ([1, 2, 2, 2], [[0, 4], [0, 1, 4], [0, 2, 4], [0, 3, 4]])
    Notes
    ------
    Edge weight attributes must be numerical and non-negative.
    Distances are calculated as sums of weighted edges traversed.
    """
    if source == target:
        return ([0], [[source]])

    length, path = nx.single_source_dijkstra(G, source, target, weight=weight)
    if target not in length:
        raise nx.NetworkXNoPath("node %s not reachable from %s" % (source, target))

    lengths = [length[target]] # the len of s to d [1]
    paths = [path[target]]     # the path of s to d [[0,4]]
    c = count()
    B = []
    G_original = G.copy()

    for i in range(1, k):
        for j in range(len(paths[-1]) - 1):
            spur_node = paths[-1][j]
            root_path = paths[-1][:j + 1]
            edges_removed = []
            for c_path in paths:
                if len(c_path) > j and root_path == c_path[:j + 1]:
                    u = c_path[j]
                    v = c_path[j + 1]
                    if G.has_edge(u, v):
                        edge_attr = G.edge[u][v]
                        G.remove_edge(u, v)
                        edges_removed.append((u, v, edge_attr))

            # print(len(root_path))
            for n in range(len(root_path) - 1):
                node = root_path[n]
                # out-edges
                for u, v, edge_attr in list(G.edges_iter(node, data=True)):
                    G.remove_edge(u, v)
                    edges_removed.append((u, v, edge_attr))
                    # print(node,u,v,edge_attr,len(G.edges()))
                if G.is_directed():
                    # in-edges
                    for u, v, edge_attr in G.in_edges_iter(node, data=True):
                        G.remove_edge(u, v)
                        edges_removed.append((u, v, edge_attr))

            spur_path_length, spur_path = nx.single_source_dijkstra(G, spur_node, target, weight=weight)
            if target in spur_path and spur_path[target]:
                total_path = root_path[:-1] + spur_path[target]
                total_path_length = get_path_length(G_original, root_path, weight) + spur_path_length[target]
                heappush(B, (total_path_length, next(c), total_path))

            for e in edges_removed:
                u, v, edge_attr = e
                G.add_edge(u, v, edge_attr)

        if B:
            (l, _, p) = heappop(B)
            lengths.append(l)
            paths.append(p)
        else:
            break

    return (lengths, paths)


def get_path_length(G, path, weight='weight'):
    length = 0
    if len(path) > 1:
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            length += G.edge[u][v].get(weight, 1)

    return length

# G=nx.complete_graph(5)
# print(k_shortest_paths(G, 0, 4, 4))
# G=nx.path_graph(5)
# length,path=nx.single_source_dijkstra(G,0,target=4,weight='weight')
# print(length)
# print(path)

