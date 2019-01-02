
class Node:

    def __init__(self, state, parent, path_cost, heuristic_dic):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        if heuristic_dic is not None:
            self.heuristic = heuristic_dic[state]
        self.depth = 0


class MapProblem:

    def __init__(self, adjacency_list, heuristic_dic, start, goal):
        self.start = start
        self.goal = goal
        self.adjacency_list = adjacency_list
        self.h = heuristic_dic

    def initial_state(self):
        return Node(self.start, None, 0, self.h)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        adjacents = []
        adj_list = self.adjacency_list
        for entry in adj_list[state]:
            adjacents.append(entry.destination)
        return sorted(adjacents)

    def cost(self, stateA, stateB):
        source = stateA
        destination = stateB
        for edge in self.adjacency_list[source]:
            if edge.destination == destination:
                return edge.cost
        return 0

    def result(self, node, action):
        source = node.state
        destination = action
        res = Node(state=destination, parent=node, path_cost=node.path_cost + self.cost(source, destination), heuristic_dic=self.h)
        return res
