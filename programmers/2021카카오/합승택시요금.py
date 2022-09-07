# programmers 2021카카오 합승택시요금

def floydwarshall(n, fares):
    m = len(fares)
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for i in range(m):
        x, y, f = fares[i]
        graph[x][y] = f
        graph[y][x] = f
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

def solution(n, s, a, b, fares):
    answer = int(1e9)

    graph = floydwarshall(n, fares)

    for k in range(1, n+1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
