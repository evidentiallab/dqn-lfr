from __future__ import print_function
import cplex
import time


class FlowConservationTreeBase(object):
    def __init__(self, graph_model):
        self.graph_model = graph_model
        self.G = self.graph_model.G
        self.number_links = self.graph_model.number_links
        self.number_nodes = self.graph_model.number_nodes
        self.directory = self.graph_model.directory
        self.file_name_draw = self.directory + ".png"
        self.c = cplex.Cplex()

    def add_constr_conservation_flow(self, src, dst_list, var_name_list, flow_name_head, flow_name_separator="f", ct_f="B"):
        k = -1
        for dst in dst_list:
            var_f = {}
            map_f_i = {}
            map_i_f = [[] for _ in range(self.number_links)]
            list_all_f = []
            k += 1
            for i in range(self.number_links):
                link = self.graph_model.int_link_dict[i]
                vf_str_a = flow_name_head + flow_name_separator + str(k) + flow_name_separator + "a" + str(i)
                vf_str_b = flow_name_head + flow_name_separator + str(k) + flow_name_separator + "b" + str(i)
                var_f[(link.node_1, link.node_2)] = vf_str_a
                var_f[(link.node_2, link.node_1)] = vf_str_b
                list_all_f.append(vf_str_a)
                list_all_f.append(vf_str_b)
                map_f_i[vf_str_a] = i
                map_f_i[vf_str_b] = i
                map_i_f[i].append(vf_str_a)
                map_i_f[i].append(vf_str_b)
            len_f = len(list_all_f)
            ctype_f = ''.join([ct_f for _ in range(len_f)])
            self.c.variables.add(types=ctype_f, names=list_all_f)

            # constraint: f <= x ( or f <= y)
            # print "vaf = ", var_f
            for i in range(self.number_links):
                for f in map_i_f[i]:
                    vector_coeff = [1, -1]
                    vector_variable = [f, var_name_list[i]]
                    sense = ["L"]
                    rhs = [0]
                    self.c.linear_constraints.add(
                        lin_expr=[
                            cplex.SparsePair(
                                ind=vector_variable, val=vector_coeff)],
                        senses=sense,
                        rhs=rhs)

            # constraint: flow conservation
            for i in range(self.number_nodes):
                node = self.graph_model.int_node_dict[i]
                vector_coeff = []
                vector_variable = []
                sense = ["E"]
                flux_enter = self.get_flux_enter(node)
                flux_exit = self.get_flux_exit(node)
                if len(flux_enter):
                    for flux in flux_enter:
                        vector_coeff.append(1)
                        vector_variable.append(var_f[flux])
                if len(flux_exit):
                    for flux in flux_exit:
                        vector_coeff.append(-1)
                        vector_variable.append(var_f[flux])
                if node == src:
                    rhs = [-1]
                elif node == dst:
                    rhs = [1]
                else:
                    rhs = [0]
                self.c.linear_constraints.add(
                    lin_expr=[cplex.SparsePair(ind=vector_variable,
                                               val=vector_coeff)],
                    senses=sense,
                    rhs=rhs)

    def get_flux_enter(self, node):
        flux_enter = []
        neighbours = self.G[node]
        for n in neighbours:
            flux_enter.append((n, node))
        return flux_enter

    def get_flux_exit(self, node):
        flux_exit = []
        neighbours = self.G[node]
        for n in neighbours:
            flux_exit.append((node, n))
        return flux_exit
