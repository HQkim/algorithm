# BOJ 10026 적록색약
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, color, n):
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, color, n)


N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            color = graph[i][j]
            visited[i][j] = 1
            dfs(i, j, color, N)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0]*N for _ in range(N)]
cnt_rg = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_rg += 1
            color = graph[i][j]
            visited[i][j] = 1
            dfs(i, j, color, N)

print(cnt, cnt_rg)