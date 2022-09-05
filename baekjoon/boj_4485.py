# BOJ 4485 녹색 옷 입은 애가 젤다지?

import sys, heapq

input = sys.stdin.readline
INF = int(10e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
numbering = 1

while 1:
    N = int(input().rstrip())
    if N == 0:
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    dist = [[INF]*N for _ in range(N)]
    
    q = []
    dist[0][0] = graph[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if cost > dist[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + graph[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
        
    print(f'Problem {numbering}: {dist[N-1][N-1]}')
    numbering += 1