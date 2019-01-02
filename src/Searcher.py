from .DataStructures import *


class Searcher:

    def backtrack(self, node):
        # prints the final path after finding the goal
        path_cost = node.path_cost
        path_stack = StackPlusExists()
        while True:
            path_stack.push(node.state)
            node = node.parent
            if node is None:
                break
        l = []
        while not path_stack.empty():
            l.append(path_stack.pop())
        print(' -> '.join(l))
        print('Path cost: ', path_cost)

    def breadth_first_search(self, problem, graph_search):
        all_visits = 0
        visited = []
        expanded_nodes = 0
        max_memory = -float('inf')

        print('Starting Breadth-First Search')
        print('Path costs do NOT matter in BFS')
        print('-------------------------------------------------------------')
        node = problem.initial_state()
        if problem.goal_test(node.state):
            return True, len(visited), all_visits, expanded_nodes, max_memory
        frontier = UnorderedNodeQueue()
        frontier.insert(node)
        all_visits += 1
        visited.append(node.state)
        explored = Explored(graph_search)
        print(frontier)
        print(explored)
        print('-------------------------------------------------------------')
        while True:
            if frontier.empty():
                return False, len(visited), all_visits, expanded_nodes, max_memory
            node = frontier.get()
            expanded_nodes += 1
            explored.insert(node)
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                if not explored.exists(child.state) and not frontier.exists(child.state):
                    all_visits += 1
                    if child.state not in visited:
                        visited.append(child.state)
                    if problem.goal_test(child.state):
                        print('FOUND {0} AFTER EXPANDING {1}'.format(child.state, node.state))
                        self.backtrack(child)
                        return True, len(visited), all_visits, expanded_nodes, max_memory
                    frontier.insert(child)
            print(frontier)
            print(explored)
            print('-------------------------------------------------------------')
            max_memory = max(max_memory, frontier.length() + explored.length())

    def uniform_cost_search(self, problem, graph_search):
        all_visits = 0
        expanded_nodes = 0
        visited = []
        max_memory = -float('inf')

        print('Starting Uniform-Cost Search')
        print('-------------------------------------------------------------')

        node = problem.initial_state()
        frontier = OrderedNodeQueue()
        frontier.insert(node, node.path_cost)
        all_visits += 1
        visited.append(node.state)
        explored = Explored(graph_search)
        print(frontier)
        print(explored)
        print('-------------------------------------------------------------')
        while True:
            if frontier.empty():
                return False, len(visited), all_visits, expanded_nodes, max_memory
            node = frontier.get()
            expanded_nodes += 1
            if problem.goal_test(node.state):
                print('FOUND, PATH:')
                self.backtrack(node)
                return True, len(visited), all_visits, expanded_nodes, max_memory
            explored.insert(node)
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                if not explored.exists(child.state) and not frontier.exists(child.state)[0]:
                    all_visits += 1
                    if child.state not in visited:
                        visited.append(child.state)
                    frontier.insert(child, child.path_cost)
                elif frontier.exists(child.state)[0]:
                    cost_in_frontier = frontier.exists(child.state)[1]
                    current_cost = child.path_cost
                    if current_cost < cost_in_frontier:
                        all_visits += 1
                        frontier.replace(child, child.path_cost)
            print(frontier)
            print(explored)
            print('-------------------------------------------------------------')
            max_memory = max(max_memory, frontier.length() + explored.length())

    def greedy_best_first_search(self, problem, graph_search):
        all_visits = 0
        expanded_nodes = 0
        visited = []
        max_memory = -float('inf')
        print('Starting Greedy Best-First Search')
        print('-------------------------------------------------------------')
        node = problem.initial_state()
        frontier = OrderedNodeQueue()
        frontier.insert(node, node.heuristic)
        all_visits += 1
        visited.append(node.state)
        explored = Explored(graph_search)
        print(frontier)
        print(explored)
        print('-------------------------------------------------------------')
        while True:
            if frontier.empty():
                return False, len(visited), all_visits, expanded_nodes, max_memory
            node = frontier.get()
            expanded_nodes += 1
            if problem.goal_test(node.state):
                print('FOUND, PATH:')
                self.backtrack(node)
                return True, len(visited), all_visits, expanded_nodes, max_memory
            explored.insert(node)
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                if not explored.exists(child.state) and not frontier.exists(child.state)[0]:
                    all_visits += 1
                    if child.state not in visited:
                        visited.append(child.state)
                    frontier.insert(child, child.heuristic)
            print(frontier)
            print(explored)
            print('-------------------------------------------------------------')
            max_memory = max(max_memory, frontier.length() + explored.length())

    def a_star_search(self, problem, graph_search):
        all_visits = 0
        expanded_nodes = 0
        visited = []
        max_memory = -float('inf')
        print('Starting A* Search')
        print('-------------------------------------------------------------')
        node = problem.initial_state()
        frontier = OrderedNodeQueue()
        frontier.insert(node, node.heuristic + node.path_cost)
        all_visits += 1
        visited.append(node.state)
        explored = Explored(graph_search)
        print(frontier)
        print(explored)
        print('-------------------------------------------------------------')
        while True:
            if frontier.empty():
                return False, len(visited), all_visits, expanded_nodes, max_memory
            node = frontier.get()
            expanded_nodes += 1
            if problem.goal_test(node.state):
                print('FOUND, PATH:')
                self.backtrack(node)
                return True, len(visited), all_visits, expanded_nodes, max_memory
            explored.insert(node)
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                if not explored.exists(child.state) and not frontier.exists(child.state)[0]:
                    all_visits += 1
                    if child.state not in visited:
                        visited.append(child.state)
                    frontier.insert(child, child.heuristic + child.path_cost)
            print(frontier)
            print(explored)
            print('-------------------------------------------------------------')
            max_memory = max(max_memory, frontier.length() + explored.length())

    def depth_first_search(self, problem, graph_search):
        all_visits = 0
        expanded_nodes = 0
        visited = []
        max_memory = -float('inf')
        print('Starting Depth-First Search')
        print('Path costs do NOT matter in DFS')
        print('-------------------------------------------------------------')
        node = problem.initial_state()
        if problem.goal_test(node.state):
            return True, len(visited), all_visits, expanded_nodes, max_memory
        frontier = StackPlusExists()
        frontier.push(node)
        all_visits += 1
        visited.append(node.state)
        explored = Explored(graph_search)
        print(frontier)
        print(explored)
        print('-------------------------------------------------------------')
        while True:
            if frontier.empty():
                return False, len(visited), all_visits, expanded_nodes, max_memory
            node = frontier.pop()
            expanded_nodes += 1
            explored.insert(node)
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                if not explored.exists(child.state) and not frontier.exists(child.state):
                    all_visits += 1
                    if child.state not in visited:
                        visited.append(child.state)
                    if problem.goal_test(child.state):
                        print('FOUND {0} AFTER EXPANDING {1}'.format(child.state, node.state))
                        self.backtrack(child)
                        return True, len(visited), all_visits, expanded_nodes, max_memory
                    frontier.push(child)
            print(frontier)
            print(explored)
            print('-------------------------------------------------------------')
            max_memory = max(max_memory, frontier.length() + explored.length())

    def iterative_deepening_tree_search(self, problem, max_depth=100):
        for l in range(max_depth):
            print('depth ', str(l), ' in progress...')
            result = self.depth_limited_tree_search(problem, l)
            if result[0] != 'Cutoff':
                self.backtrack(result[1])
                return result
            else:
                print('Cutoff!')
        print('iterative deepening found no answer')

    def depth_limited_tree_search(self, problem, limit):
        return self.recursive_DLS_tree(problem.initial_state(), problem, limit)

    def recursive_DLS_tree(self, node, problem, limit):
        if problem.goal_test(node.state):
            return True, node
        elif limit == 0:
            return 'Cutoff', None
        else:
            cutoff_occured = False
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                result = self.recursive_DLS_tree(child, problem, limit-1)
                if result[0] == 'Cutoff':
                    cutoff_occured = True
                elif result[0] != False:
                    return result
            if cutoff_occured:
                return 'Cutoff', None
            return False, None

    def iterative_deepening_graph_search(self, problem, max_depth=100):
        for l in range(max_depth):
            print('depth ', str(l), ' in progress...')
            result, visited_nodes, all_visits, expanded_nodes = self.depth_limited_graph_search(problem, l)
            if result == 'Cutoff':
                print('Cutoff!')
                print('Expanded {0} nodes'.format(expanded_nodes))
                print('Visited {0} nodes'.format(visited_nodes))
                print('All visits: {0}'.format(all_visits))
                print('-------------------------------------------------------------')
            elif result == True:
                print('FOUND!')
                print('Expanded {0} nodes'.format(expanded_nodes))
                print('Visited {0} nodes'.format(visited_nodes))
                print('All visits: {0}'.format(all_visits))
                print('-------------------------------------------------------------')
                break
            else:
                print('iterative deepening found no answer')
                break

    def depth_limited_graph_search(self, problem, limit):
        all_visits = 0
        expanded_nodes = 0
        visited = []
        frontier = StackPlusExists()
        node = problem.initial_state()
        frontier.push(node)
        all_visits += 1
        visited.append(node.state)
        explored = Explored(True)

        while True:
            if frontier.empty():
                return False, len(visited), all_visits, expanded_nodes

            if not frontier.something_left_in_depth(limit):
                return 'Cutoff', len(visited), all_visits, expanded_nodes

            node = frontier.pop_node_within_limit(limit)
            expanded_nodes += 1
            explored.insert(node)
            for action in problem.actions(node.state):
                child = problem.result(node, action)
                if not explored.exists(child.state) and not frontier.exists(child.state):
                    all_visits += 1
                    child.depth = node.depth + 1
                    if child.state not in visited:
                        visited.append(child.state)
                    if problem.goal_test(child.state):
                        print('FOUND {0} AFTER EXPANDING {1}'.format(child.state, node.state))
                        self.backtrack(child)
                        return True, len(visited), all_visits, expanded_nodes
                    frontier.push(child)
            print(frontier)
            print(explored)
            print()
