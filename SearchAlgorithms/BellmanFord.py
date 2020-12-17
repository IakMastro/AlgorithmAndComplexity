def bellman_ford(graph, source):
    distance, predecessor = dict(), dict()

    for node in graph:
        distance[node], predecessor[node] = float('inf'), None

    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle"

    return distance, predecessor