# 인터넷 참고

from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if(visited[i] == 0 and graph[v][i] == 1):
            dfs(i, visited)


def bfs(v, visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1


visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)


dfs(v, visited_dfs)
print()
bfs(v, visited_bfs)
