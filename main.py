import argparse
from GraphMaker import GraphMaker
from Handler import Handler


def main():
    parser = argparse.ArgumentParser(description='Run your desired search algorithm on a graph :)')
    parser.add_argument('--algorithm', type=str, help='BFS / DFS / UniformCost / A* / GreedyBestFirst', required=True)
    parser.add_argument('--graphFile', type=str, help='The path to .txt file containing your graph.', required=True)
    parser.add_argument('--heuristicFile', type=str, help='The path to .txt file containing your heuristics.', required=False, default=None)
    parser.add_argument('--startNode', type=str, required=True)
    parser.add_argument('--goalNode', type=str, required=True)
    parser.add_argument('--treeSearch', help='Use this switch if you want to perform tree search rather than graph search', action='store_true')
    args = parser.parse_args()
    algo = args.algorithm
    graph_file = args.graphFile
    heu_file = args.heuristicFile
    start_node = args.startNode
    goal_node = args.goalNode
    graph_search = not args.treeSearch
    gm = GraphMaker(graph_file, heu_file)
    heuristic_dict = gm.get_heuristic_dictionary()
    adjacency_list = gm.get_adjacency_list()
    h = Handler(algo, adjacency_list, heuristic_dict, start_node, goal_node, graph_search)
    h.handle()


if __name__ == '__main__':
    main()
