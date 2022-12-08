from __future__ import print_function
import time
from cplex.exceptions import CplexSolverError
from ILP.Graph_generator import GraphGeneratorGrid2D
from ILP.flow_conservation_tree import FlowConservationTreeBase
import cplex


class SimpleSteinerTree(FlowConservationTreeBase):
    def __init__(self, graph_model):
        FlowConservationTreeBase.__init__(self, graph_model)
        self.graph_model = graph_model
        self.str_time = self.graph_model.str_time
        self.directory = self.graph_model.directory
        self.file_name_draw = self.directory+ 'simple_steiner.png'

        self.var_x = []
        for i in range(self.number_links):
            self.var_x.append("x" + str(i))
        self.var_node = []

    def declare_optimization_objective(self):
        self.c.objective.set_sense(self.c.objective.sense.minimize)
        obj_func = [self.graph_model.get_link_weight_int(i)
                    for i in range(self.number_links)]
        ctype = ''.join(["B" for _ in range(self.number_links)])
        self.c.variables.add(obj=obj_func, types=ctype,
                             names=self.var_x)

    def add_constr_conservation_flow_x(self):
        src = self.graph_model.src_node
        dst_list = self.graph_model.dst_list
        self.add_constr_conservation_flow(src, dst_list, self.var_x, "")
    '''
    https://hal.archives-ouvertes.fr/inria-00504914/document
    '''
    def add_other_constraints(self):
        for i in range(self.number_nodes):
            self.var_node.append("c" + str(i))
        ctype_c = ''.join(["B" for i in range(self.number_nodes)])
        self.c.variables.add(types=ctype_c, names=self.var_node)

        # Constraint: Each vertex from S is in the tree
        for node in self.graph_model.steiner_nodes:
            vector_coeff = []
            vector_variable = []
            sense = ["G"]
            rhs = [1]
            flux_enter = self.get_flux_enter(node)
            for flux in flux_enter:
                vector_coeff.append(1)
                vector_variable.append(self.var_x[self.graph_model.n1n2_link_dict[flux].link_id])
            self.c.linear_constraints.add(
                lin_expr=[cplex.SparsePair(ind=vector_variable,
                                           val=vector_coeff)],
                senses=sense,
                rhs=rhs)

        # Constraint: |V| - |E| = 1
        vector_coeff = []
        vector_variable = []
        sense = ["E"]
        rhs   = [1]
        for i in range(self.number_nodes):
            vector_coeff.append(1)
            vector_variable.append(self.var_node[i])
        for i in range(self.number_links):
            vector_coeff.append(-1)
            vector_variable.append(self.var_x[i])
        self.c.linear_constraints.add(
            lin_expr=[cplex.SparsePair(ind=vector_variable,
                                       val=vector_coeff)],
            senses=sense,
            rhs=rhs)

        # Constraint: c(e[0]) >= b(e) and c(e[1]) >= b(e)
        for j in range(self.number_links):
            link = self.graph_model.int_link_dict[j].tuple
            for k in [0, 1]:
                vector_coeff = [1, -1]
                vector_variable = [self.var_x[j], self.var_node[self.graph_model.node_int_dict[link[k]]]]
                sense = ["L"]
                rhs = [0]
                self.c.linear_constraints.add(
                    lin_expr=[cplex.SparsePair(ind=vector_variable,
                                               val=vector_coeff)],
                    senses=sense,
                    rhs=rhs)

        var_F = {}
        map_F_i = {}
        map_i_F = [[] for _ in range(self.number_links)]
        list_all_F = []
        for i in range(self.number_links):
            link = self.graph_model.int_link_dict[i].tuple
            vF_str_a = "F" + "a" + str(i)
            vF_str_b = "F" + "b" + str(i)
            var_F[(link[0], link[1])] = vF_str_a
            var_F[(link[1], link[0])] = vF_str_b
            list_all_F.append(vF_str_a)
            list_all_F.append(vF_str_b)
            map_F_i[vF_str_a] = i
            map_F_i[vF_str_b] = i
            map_i_F[i].append(vF_str_a)
            map_i_F[i].append(vF_str_b)
        len_F = len(list_all_F)
        ub = [cplex.infinity for _ in range(len_F)]
        lb = [0 for _ in range(len_F)]
        ctype_F = ''.join(["C" for _ in range(len_F)])
        self.c.variables.add(types=ctype_F, ub=ub, lb=lb, names=list_all_F)
        # for F in list_all_F[0:1]:
            # print(self.c.variables.get_upper_bounds(F))
            # print(self.c.variables.get_lower_bounds(F)

        # Each edge sends a flow of 2 if it is taken
        for i in range(self.number_links):
            vector_coeff = [1, 1, -2]
            vector_variable = [map_i_F[i][0], map_i_F[i][1], self.var_x[i]]
            sense = ["E"]
            rhs = [0]
            self.c.linear_constraints.add(
                lin_expr=[cplex.SparsePair(ind=vector_variable,
                                           val=vector_coeff)],
                senses=sense,
                rhs=rhs)

        # Vertices receive strictly less than 2
        for i in range(self.number_nodes):
            vector_coeff = []
            vector_variable = []
            sense = ["L"]
            rhs = [2 - float(2) / self.number_links]
            node = self.graph_model.int_node_dict[i]
            flux_enter = self.get_flux_enter(node)
            for flux in flux_enter:
                vector_coeff.append(1)
                vector_variable.append(var_F[flux])
            self.c.linear_constraints.add(
                lin_expr=[cplex.SparsePair(ind=vector_variable,
                                           val=vector_coeff)],
                senses=sense,
                rhs=rhs)

    def main(self, time_limit=120, plot=False):
        self.declare_optimization_objective()
        self.add_constr_conservation_flow_x()
        self.add_other_constraints()
        self.c.parameters.timelimit.set(time_limit + 10)
        start_time = time.time()
        self.c.write(self.directory+"_generated.lp", "lp")

        try:
            self.c.solve()
        except CplexSolverError:
            print("Exception raised during solve")
            return
        status = self.c.solution.get_status()
        # print(self.c.solution.status[status])
        if status == self.c.solution.status.unbounded:
            print("Model is unbounded")
            return
        if status == self.c.solution.status.infeasible:
            print("Model is infeasible")
            return
        if status == self.c.solution.status.infeasible_or_unbounded:
            print("Model is infeasible or unbounded")
            return
        objective_value = self.c.solution.get_objective_value()
        elasped_time = time.time() - start_time
        if elasped_time >= time_limit:
            return None
        # print("Solution value  = ", self.c.solution.get_objective_value())
        res = []
        cost = 0
        for i in range(self.number_links):
            if self.c.solution.get_values(self.var_x[i]) == 1:
                res.append(i)
                cost += self.graph_model.get_link_weight_int(i)
        if plot:
            self.graph_model.draw_and_save_simple_steiner_tree(res,
            self.file_name_draw,self.graph_model.src_node,self.graph_model.dst_node)
        return cost

if __name__ == '__main__':
    SimpleSteinerTree(GraphGeneratorGrid2D(5, 5, 2, 10)).main(plot=True)

