clock = 0


def dfs(node, graph, visited=None, preorder=None, postorder=None):
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
            dfs(neighbour_node, graph, visited, preorder, postorder)

        postorder[node] = clock
        clock += 1

    return visited, preorder, postorder
