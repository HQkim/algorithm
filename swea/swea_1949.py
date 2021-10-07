# swea 1949 등산로 조성

def f(row, col, s, is_dig):
    global max_s, K, N
    max_s = max(max_s, s)

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni = row + di
        nj = col + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if graph[row][col] > graph[ni][nj]:
                visited[ni][nj] = 1
                f(ni, nj, s+1, is_dig)
                visited[ni][nj] = 0
            else:
                if not is_dig and graph[ni][nj]-graph[row][col] < K:
                    diff = graph[ni][nj] - graph[row][col]
                    graph[ni][nj] -= (diff + 1)
                    visited[ni][nj] = 1
                    f(ni, nj, s+1, 1)
                    graph[ni][nj] += (diff + 1)
                    visited[ni][nj] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    max_h = 0
    for i in range(N):
        max_h = max(max_h, max(graph[i]))

    max_s = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_h:
                visited[i][j] = 1
                f(i, j, 1, 0)
                visited[i][j] = 0

    print(f'#{tc} {max_s}')
