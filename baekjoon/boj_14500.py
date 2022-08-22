# BOJ 14500 테트로미노

import sys


def dfs(x, y, move, cnt):
    global max_cnt

    if move == 3:
        max_cnt = max(max_cnt, cnt)
        return

    if max_cnt >= cnt + max_val * (3 - move):
        return
    
    for k in range(4):
        nx = x + d[k][0]
        ny = y + d[k][1]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if move == 1:       # ㅜ 모양을 처리하기 위해서 x, y 에서 다시 탐색
                visited[nx][ny] = 1
                dfs(x, y, move+1, cnt+graph[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, move+1, cnt+graph[nx][ny])
            visited[nx][ny] = 0


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_cnt = 0
max_val = max(map(max, graph))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = 0

print(max_cnt)