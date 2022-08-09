# BOJ 2606 바이러스
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
queue = deque([1])
visited[1] = True

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
    
count = 0
for i in visited:
    if i == True:
        count += 1

print(count-1)