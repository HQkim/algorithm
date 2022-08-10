# BOJ 11724 연결 요소의 개수
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, v):
    visited[v] = 1

    for u in graph[v]:
        if not visited[u]:
            dfs(graph, visited, u)


N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(graph, visited, i)

print(cnt)