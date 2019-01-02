class Explored:

    def __init__(self, graph_search):
        self.q = []
        self.graph_search = graph_search

    def insert(self, node):
        self.q.append(node)

    def exists(self, state):
        if self.graph_search:
            for node in self.q:
                if node.state == state:
                    return True
            return False
        else:
            return False

    def length(self):
        if self.graph_search:
            return len(self.q)
        return 0

    def __repr__(self):
        if not self.graph_search:
            return 'Explored: Tree search has no explored set'
        r = 'Explored: ['
        for i in range(0, len(self.q)):
            r += self.q[i].state
            if i != len(self.q) - 1:
                r += ', '
        r += ']'
        return r


class StackPlusExists:

    def __init__(self):
        self.q = []

    def empty(self):
        return len(self.q) == 0

    def push(self, node):
        self.q.append(node)

    def exists(self, state):
        for node in self.q:
            if node.state == state:
                return True
        return False

    def pop(self):
        res = self.q[-1]
        del self.q[-1]
        return res

    def length(self):
        return len(self.q)

    def something_left_in_depth(self, limit):
        for node in self.q:
            if node.depth < limit:
                return True
        return False

    def pop_node_within_limit(self, limit):

        node_idx = -1
        for i in range(len(self.q)):
            node = self.q[i]
            if node.depth < limit:
                min_depth = node.depth
                node_idx = i
        temp = self.q[node_idx]
        del self.q[node_idx]
        return temp


    def __repr__(self):
        r = 'Frontier: ['
        for i in range(0, len(self.q)):
            r += self.q[i].state + ' ' + str(self.q[i].path_cost)
            if i != len(self.q) - 1:
                r += ', '
        r += ']'
        return r


class UnorderedNodeQueue:

    def __init__(self):
        self.q = []

    def empty(self):
        return len(self.q) == 0

    def insert(self, node):
        self.q.append(node)

    def get(self):
        res = self.q[0]
        del self.q[0]
        return res

    def exists(self, state):
        for node in self.q:
            if node.state == state:
                return True
        return False

    def length(self):
        return len(self.q)

    def __repr__(self):
        r = 'Frontier: ['
        for i in range(0, len(self.q)):
            r += self.q[i].state + ' ' + str(self.q[i].path_cost)
            if i != len(self.q) - 1:
                r += ', '
        r += ']'
        return r


class OrderedNodeQueue:

    def __init__(self):
        self.q = []

    def empty(self):
        return len(self.q) == 0

    def insert(self, node, num):
        self.q.append((node, num))

    def exists(self, state):
        for pair in self.q:
            if pair[0].state == state:
                return True, pair[0].path_cost
        return False, -1

    def get(self):
        current_min_pair = (None, float('inf'))
        current_min_pair_index = -1

        for pair in self.q:
            node_cost = pair[1]
            if node_cost < current_min_pair[1]:
                current_min_pair_index = self.q.index(pair)
                current_min_pair = pair
        del self.q[current_min_pair_index]
        return current_min_pair[0]

    def replace(self, new, newcost):
        idx = -1
        for pair in self.q:
            if pair[0].state == new.state:
                idx = self.q.index(pair)
                break
        del self.q[idx]
        self.insert(new, newcost)

    def length(self):
        return len(self.q)

    def __repr__(self):
        r = 'Frontier: ['
        for i in range(0, len(self.q)):
            r += self.q[i][0].state + ' ' + str(self.q[i][1])
            # r += ' (parent: %s) ' % self.q[i][0].parent.state
            if i != len(self.q) - 1:
                r += ', '
        r += ']'
        return r


