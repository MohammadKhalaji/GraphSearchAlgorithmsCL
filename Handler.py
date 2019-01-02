from src.MapProblem import MapProblem
from src.Searcher import Searcher


class Handler:
    def __init__(self, algorithm, adjacency_list, heuristic_dict, start, goal, graph_search):
        self.algorithm = algorithm
        self.adjacency_list = adjacency_list
        self.heuristic_dict = heuristic_dict
        self.start = start
        self.goal = goal
        self.graph_search = graph_search

    def handle(self):
        possible_algorithms = ['dfs', 'bfs', 'a*', 'greedybestfirst', 'uniformcost']
        if self.heuristic_dict is None:
            possible_algorithms = ['dfs', 'bfs', 'uniformcost']

        if self.algorithm.lower() not in possible_algorithms:
            print('This algorithm is not possible for your inputs. Please specify the heuristics file')
            exit(0)

        mp = MapProblem(self.adjacency_list, self.heuristic_dict, self.start, self.goal)
        searcher = Searcher()

        if self.algorithm.lower() == 'dfs':
            searcher.depth_first_search(mp, self.graph_search)
        elif self.algorithm.lower() == 'bfs':
            searcher.breadth_first_search(mp, self.graph_search)
        elif self.algorithm.lower() == 'a*':
            searcher.a_star_search(mp, self.graph_search)
        elif self.algorithm.lower() == 'greedybestfirst':
            searcher.greedy_best_first_search(mp, self.graph_search)
        elif self.algorithm.lower() == 'uniformcost':
            searcher.uniform_cost_search(mp, self.graph_search)
