# GraphSearchAlgorithmsCL
A command line program to run search algorithms.

## Prerequisites
* A .txt file containing the edges of your graph.
Adjacency of nodes A, B are stated like "A B" in the file and there is NO need to put a line containing "B A".

If graph edges are not weighted, lines of the file should be like this:
```
Oradea Zerind
Oradea Sibiu
Zerind Arad
Arad Sibiu
```

And if edges are weighted:
```
Oradea Zerind 71
Oradea Sibiu 151
Zerind Arad 75
Arad Sibiu 140
```

* Another .txt file containing heuristic value of each node (used in A* and GBFS algorithms)
Example:
```
Arad 366
Bucharest 0
Craiova 160
Dobreta 242
Eforie 161
```

## Algorithms
Both Graph-Search and Tree-Search versions of algorithms below are implemented.

* Depth-First Search: DFS
* Breadth-First Search: BFS
* Uniform-Cost Search: UniformCost
* Greedy Best-First Search: GreedyBestFirst
* A-start Search: A*


## How to use
Just run the `main.py` file with arguments like this.

* Graph search:
```
python main.py --algorithm a* --graphFile graph.txt --heuristicFile heu.txt --startNode Arad --goalNode Bucharest
```

* Tree search:
```
python main.py --algorithm a* --graphFile graph.txt --heuristicFile heu.txt --startNode Arad --goalNode Bucharest --treeSearch
```
