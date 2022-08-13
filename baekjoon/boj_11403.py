import sys

input = sys.stdin.readline

def dfs(v):
    for u in graph[v]:
        if not visited[u]:
            visited[u] = 1
            dfs(u)

N = int(input())
graph = [[idx for idx, value in enumerate(map(int, input().split())) if value == 1] for _ in range(N)]

for i in range(N):
    visited = [0]*N
    dfs(i)
    print(*visited)

