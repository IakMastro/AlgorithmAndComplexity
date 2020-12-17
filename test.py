from SearchAlgorithms.DFS import dfs
from SearchAlgorithms.BFS import bfs
from SearchAlgorithms.Dijsktra import dijkstra
from SearchAlgorithms.BellmanFord import bellman_ford

if __name__ == '__main__':
    graph = {
        "1": {"2", "3"},
        "2": {"1"},
        "3": {"1", "4", "5"},
        "4": {"3"},
        "5": {"3"}
    }

    graph_with_cost = {
        "1": {"2": 4, "4": 8},
        "2": {"3": 8, "4": 11},
        "3": {"5": 8, "7": 4, "8": 7},
        "4": {"1": 8, "2": 11, "5": 7, "6": 1},
        "5": {"3": 8, "4": 7, "6": 6},
        "6": {"4": 1, "5": 6, "7": 7},
        "7": {"3": 4, "6": 7, "8": 14, "9": 10},
        "8": {"3": 7, "7": 14, "9": 9},
        "9": {"7": 10, "8": 9}
    }

    visited, preorder, postorder = dfs("1", graph)
    # visited, preorder = bfs("1", graph)

    print(f"Printing visited: {visited}")
    print(f"Printing preorder: {preorder}")
    print(f"Printing postorder: {postorder}")

    # distance, predecessor = dijkstra(graph_with_cost, "1")
    distance, predecessor = bellman_ford(graph_with_cost, "1")

    if distance is None:
        print("There is a negative value in the graph. Use Bellman Ford instead.")

    else:
        print(f"Printing distances: {distance}")
        print(f"Printing predecessors: {predecessor}")
