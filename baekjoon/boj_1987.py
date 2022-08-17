# BOJ 1987 알파벳

import sys

input = sys.stdin.readline

def dfs(x, y, d):
    global max_d
    max_d = max(max_d, d)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not check[ord(graph[nx][ny])-65]:
            check[ord(graph[nx][ny])-65] = 1
            dfs(nx, ny, d+1)       
            check[ord(graph[nx][ny])-65] = 0
    

R, C = map(int, input().split())
graph = [input().rstrip() for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

max_d = 0
check = [0]*26
check[ord(graph[0][0])-65] = 1
dfs(0, 0, 1)

print(max_d)