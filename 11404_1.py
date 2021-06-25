# 11404번

import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            tmp = graph[i][k]+graph[k][j]
            if graph[i][j] > tmp:
                graph[i][j] = tmp

for i in range(1, n+1):
    for j in range(1, n+1):
        cost = graph[i][j]
        if cost == INF:
            print(0, end=" ")
        else:
            print(cost, end=" ")
    print()
