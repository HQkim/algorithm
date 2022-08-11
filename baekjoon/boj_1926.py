# BOJ 1926 그림
import sys
from collections import deque

def bfs(i, j, n, m):
    q = deque([(i, j)])
    graph[i][j] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + direc[i][0]
            ny = y + direc[i][1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                cnt += 1
                q.append((nx, ny))
                graph[nx][ny] = 0

    return cnt

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

total = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            total += 1
            max_area = max(max_area, bfs(i, j, n, m))

print(total)
print(max_area)