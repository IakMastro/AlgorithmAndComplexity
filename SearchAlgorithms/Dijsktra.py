def dijkstra(graph, source):
    distance, predecessor = dict(), dict()

    for node in graph:
        distance[node], predecessor[node] = float('inf'), None

    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if graph[node][neighbour] < 0:
                    return None, None

                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    return distance, predecessor