# BOJ 4963 섬의 개수
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

def dfs(graph, visited, x, y, r, c):
    visited[x][y] = 1

    d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for i in range(8):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(graph, visited, nx, ny, r, c)



while 1:

    col, row = map(int, input().split())

    if col == 0 and row == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0]*col for _ in range(row)]

    cnt = 0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and graph[i][j] == 1:
                cnt += 1
                dfs(graph, visited, i, j, row, col)
    
    print("{}\n".format(cnt))