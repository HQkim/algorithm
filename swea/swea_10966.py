# swea 10966 물놀이를 가자
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    queue = deque([])

    for i in range(N):                  # 물인 곳 출발지로
        for j in range(M):
            if graph[i][j] == 'W':
                queue.append((i, j, 0))
                visited[i][j] = -1

    while queue:                        # bfs
        i, j, d = queue.popleft()

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                queue.append((ni, nj, d+1))
                visited[ni][nj] = d+1

    ans = 0                             # 물이 아닌곳 거리 더하기
    for i in range(N):
        for j in range(M):
            if visited[i][j] != -1:
                ans += visited[i][j]

    print(f'#{tc} {ans}')
