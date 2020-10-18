# 인터넷 참고

from collections import deque

n, m = map(int, input().split())
v = list(map(int, input().split()))
v.sort()

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    if graph[a][b] == 0 and graph[b][a] == 0:
        graph[a][b] = 1 
        graph[b][a] = -1
    else :
        graph[a][b] = 1


def bfs(v, visited):
    queue = deque([v[0]])
    visited[v[0]] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v[0]][i] == 1:
                queue.append(i)
                visited[i] = 1


visited = [0]*(n+1)


bfs(v, visited)