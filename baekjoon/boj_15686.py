# BOJ 15686 치킨 배달
from itertools import combinations

INF = int(10e9)
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

houses = []
stores = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        if graph[i][j] == 2:
            stores.append((i, j))

H = len(houses)
S = len(stores)
distances = [[0]*S for _ in range(H)]

for i in range(H):
    for j in range(S):
        distances[i][j] = (abs(houses[i][0] - stores[j][0]) + abs(houses[i][1] - stores[j][1]), j)
    distances[i].sort(key=lambda x: x[0])

combs = combinations(range(S), M)

min_total = INF
for comb in combs:
    total = 0
    for d in distances:
        for j in range(S):
            if d[j][1] in comb:
                min_d = d[j][0]
                break
        total += min_d
    min_total = min(min_total, total)

print(min_total)
