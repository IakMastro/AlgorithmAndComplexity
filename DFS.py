graph = {
    "1": {"2", "3"},
    "2": {"1"},
    "3": {"1", "4", "5"},
    "4": {"3"},
    "5": {"3"}
}

clock = 0


def DFS(node, visited=None, preorder=None, postorder=None):
    global clock
    if visited is None and preorder is None and postorder is None:
        visited = []
        preorder = {}
        postorder = {}

    if node not in visited:
        visited.append(node)
        preorder[node] = clock
        clock += 1

        for neighbour_node in graph[node]:
            DFS(neighbour_node, visited, preorder, postorder)

        postorder[node] = clock
        clock += 1

    return visited, preorder, postorder
