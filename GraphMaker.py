class Edge:

    def __init__(self, destination, cost):
        self.destination = destination
        self.cost = cost


class GraphMaker:

    def __init__(self, graph_file, heu_file=None):
        self.graph_file = graph_file
        self.heu_file = heu_file
        self.nodes = []
        self.heuristic_dictionary = dict()
        self.adjacency_list = dict()
        self.initialize()

    def get_heuristic_dictionary(self):
        if self.heu_file is None:
            return None
        return self.heuristic_dictionary

    def get_adjacency_list(self):
        return self.adjacency_list

    def initialize(self):

        gf = open(self.graph_file, 'r')
        graph_lines = gf.readlines()
        for line in graph_lines:
            if line != '':
                if len(line.split(' ')) != 3:
                    line += ' 1'
                a, b, cost = line.split(' ')
                a = a.replace(' ', '')
                a = a.replace('\n', '')
                b = b.replace(' ', '')
                b = b.replace('\n', '')
                if a not in self.adjacency_list.keys():
                    self.adjacency_list[a] = []
                if b not in self.adjacency_list.keys():
                    self.adjacency_list[b] = []
                cost = float(cost)

                self.adjacency_list[a].append(Edge(destination=b, cost=cost))
                self.adjacency_list[b].append(Edge(destination=a, cost=cost))
        gf.close()

        if self.heu_file is not None:
            hf = open(self.heu_file, 'r')
            heu_lines = hf.readlines()
            for line in heu_lines:
                if line != '':
                    node, heu = line.split(' ')
                    heu = float(heu)
                    node = node.replace(' ', '')
                    node = node.replace('\n', '')
                    self.heuristic_dictionary[node] = heu
            hf.close()
