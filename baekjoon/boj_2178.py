# BOJ 2178 미로 탐색

from collections import deque

N, M = map(int, input().split())

graph = [input().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

now = (0, 0, 1)
visited[0][0] = 1

queue = deque([now])
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y, d = queue.popleft()
    if x == N-1 and y == M-1:
        break

    for i in range(4):
        nx = x + direc[i][0]
        ny = y + direc[i][1]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == '1':
            queue.append((nx, ny, d+1))
            visited[nx][ny] = 1

print(d)


