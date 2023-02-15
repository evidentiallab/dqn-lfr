from __future__ import print_function
import time
import cplex
from cplex.exceptions import CplexSolverError
from ILP.Graph_generator import GraphGeneratorGrid2D
from ILP.simple_steiner_tree import SimpleSteinerTree


class LoadBalancingSteinerTree(SimpleSteinerTree):
    def __init__(self, graph_model, beta):
        SimpleSteinerTree.__init__(self, graph_model)
        self.str_time = self.graph_model.str_time
        self.directory = self.graph_model.directory
        self.file_name_draw = self.directory + 'load_balancing.png'

        self.var_max_link_residual_bw = 'maxLinkResidualBw'
        self.var_min_link_residual_bw = 'minLinkResidualBw'
        self.beta = beta
        self.var_x = []
        for i in range(self.number_links):
            self.var_x.append("x" + str(i))
        self.var_lb = [self.var_max_link_residual_bw, self.var_min_link_residual_bw]

    def declare_optimization_objective(self):
        self.c.objective.set_sense(self.c.objective.sense.minimize)
        obj_func = [self.graph_model.get_link_weight_int(i)
                    for i in range(self.number_links)] + [self.beta, -1 * self.beta]
        ctype = ''.join(["B" for _ in range(self.number_links)] + ['I', 'I'])
        self.c.variables.add(obj=obj_func,
                             types=ctype,
                             names=self.var_x + self.var_lb)

    def add_constr_load_balancing(self):
        for link_id, link in self.graph_model.int_link_dict.items():
            vector_coeff = []
            vector_variable = []
            sense = ["L"]
            x = self.var_x[link_id]
            vector_variable.append(x)
            vector_coeff.append(-1)
            vector_variable.append(self.var_max_link_residual_bw)
            vector_coeff.append(-1)
            rhs = [-1 * link.bw]
            self.c.linear_constraints.add(lin_expr=[cplex.SparsePair(ind=vector_variable, val=vector_coeff)],
                                          senses=sense,
                                          rhs=rhs)

        for link_id, link in self.graph_model.int_link_dict.items():
            vector_coeff = []
            vector_variable = []
            sense = ["L"]
            x = self.var_x[link_id]
            vector_variable.append(x)
            vector_coeff.append(1)
            vector_variable.append(self.var_min_link_residual_bw)
            vector_coeff.append(1)
            rhs = [1 * link.bw]
            self.c.linear_constraints.add(lin_expr=[cplex.SparsePair(ind=vector_variable, val=vector_coeff)],
                                          senses=sense,
                                          rhs=rhs)

    def main(self, time_limit=120, plot=False):
        self.declare_optimization_objective()
        self.add_constr_conservation_flow_x()
        self.add_other_constraints()
        self.add_constr_load_balancing()
        self.c.parameters.timelimit.set(time_limit + 10)
        self.c.write(self.directory + "_generated.lp", "lp")
        start_time = time.time()
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
        # objective_value = self.c.solution.get_objective_value()
        # print(objective_value)
        elasped_time = time.time() - start_time
        if elasped_time >= time_limit:
            return None
        # print("Solution value  = ", self.c.solution.get_objective_value())
        res = []
        cost = 0
        for i in range(self.number_links):
            if self.c.solution.get_values(self.var_x[i]) == 1:
                res.append(i)
                # self.graph_model.int_link_dict[i].consume_bw(1, self.graph_model.G)
                cost += self.graph_model.get_link_weight_int(i)

        if plot:
            self.graph_model.draw_and_save_load_balancing_steiner_tree(res,
         self.file_name_draw,self.graph_model.src_node,self.graph_model.dst_node)
        return cost, res,elasped_time


if __name__ == '__main__':
    print(LoadBalancingSteinerTree((GraphGeneratorGrid2D(5, 5, 2, 20)), 100).main(plot=True))
