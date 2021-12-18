# boj 2468 안전영역
import sys

sys.setrecursionlimit(10000)

def dfs(row, col, N):
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = row + di
        nj = col + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and graph[ni][nj] == 1:
            visited[ni][nj] = 1
            dfs(ni, nj, N)

N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
max_h = 0

for i in range(N):
    max_h = max(max_h, max(heights[i]))

max_area_count = 1
for h in range(1, max_h):
    graph = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    area_count = 0

    for i in range(N):
        for j in range(N):
            if heights[i][j] > h:
                graph[i][j] = 1

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] == 1:
                area_count += 1
                visited[i][j] = 1
                dfs(i, j, N)    

    max_area_count = max(max_area_count, area_count)

print(max_area_count)