import random

class Link:
    def __init__(self, link_id, node_1, node_2, weight, bw):
        self.node_1 = node_1
        self.node_2 = node_2
        self.link_id = link_id
        self.weight = weight
        self.bw = bw
        self.tuple = (node_1, node_2)

    def consume_bw(self, bw_consumed, G):
        self.bw -= bw_consumed
        assert self.bw >= 0
        G.edge[self.node_1][self.node_2]['bw'] = self.bw

    # def consume_random_bw(self, G):
    #     random_bw = random.randint(1, self.bw)
    #     self.consume_bw(random_bw, G)

    def restore_bw(self, bw_to_restore, G):
        self.consume_bw(-1 * bw_to_restore, G)


