def BFS(node):
    graph = {
        "1": {"2", "3"},
        "2": {"1"},
        "3": {"1", "4", "5"},
        "4": {"3"},
        "5": {"3"}
    }

    clock = 0
    queue = []
    preorder = {}
    visited = [node]

    queue.append(node)
    preorder[node] = clock
    clock += 1

    while queue:
        s = queue.pop(0)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                preorder[neighbour] = clock
                clock += 1
                queue.append(neighbour)

    return visited, preorder
