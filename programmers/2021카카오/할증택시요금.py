def floydwarshall(n, fares):
    m = len(fares)
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for i in range(m):
        a, b, c = fares[i]
    graph[a][b] = c
    graph[b][a] = c

    x, y, f = fares[i]
    graph[x][y] = f
    graph[y][x] = f

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


def solution(n, s, a, b, fares):

    answer = 0
    INF = int(1e9)

    graph_fares = [[INF] * (n+1) for _ in range(n+1)]
    for x in range(1, n+1):
        for y in range(1, n+1):
            if x == y:
                graph_fares[x][y] = 0

    for i in range(len(fares)):
        x, y, z = fares[i]
        graph_fares[x][y] = z
        graph_fares[y][x] = z

    graph = floydwarshall(n, fares)

    cost_min = graph[s][a] + graph[s][b]
    sep_pos = s

    for i in range(1, n+1):
        cost = graph[s][i] + graph[i][a] + graph[i][b]
        if cost < cost_min:
            cost_min = cost

    answer = cost

    # answer = graph[s][sep_pos] + graph[sep_pos][a] + graph[sep_pos][b]

    answer = int(1e9)

    graph = floydwarshall(n, fares)

    for k in range(1, n+1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
