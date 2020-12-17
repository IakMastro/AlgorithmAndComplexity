def bfs(node, graph):
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
