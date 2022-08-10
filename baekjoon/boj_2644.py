# BOJ 2644 촌수계산

from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
q = deque([(x, 0)])
visited = [0]*(n+1)
visited[x] = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

while q:
    now, dist = q.popleft()

    if now == y:
        break

    for i in graph[now]:
        if not visited[i]:
            visited[i] = 1
            q.append((i, dist+1))

if now == y:
    print(dist)
else:
    print(-1)
