# BOJ 1197 최소 스패닝 트리

import sys

#### 크루스칼 알고리즘 ####
def find_parent(x):
    while parents[x] != x:
        x = parents[x]
    return x


def union(x, y):
    x_parent = find_parent(x)
    y_parent = find_parent(y)
    if x_parent <= y_parent:
        parents[y_parent] = x_parent
    else:
        parents[x_parent] = y_parent


if __name__ == '__main__':
    input = sys.stdin.readline
    V, E = map(int, input().rstrip().split())
    parents = [i for i in range(V+1)]
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        edges.append((a, b, c))

    edges.sort(key=lambda x: x[2])
    weight = 0
    cnt = 0
    for edge in edges:
        a, b, c = edge
        if find_parent(a) != find_parent(b):
            cnt += 1
            weight += c
            union(a, b)
        if cnt == V - 1:
            break

    print(weight)



#### 프림 알고리즘 ####
# INF = int(10e9)
# V, E = map(int, input().split())
# graph = [[] for _ in range(V + 1)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))

# visited = [0] * (V + 1)
# distance = [INF] * (V + 1)
# distance[0], distance[1] = 0, 0

# for i in range(V):
#     min_dist = INF
#     for j in range(1, V + 1):
#         if not visited[j] and distance[j] <= min_dist:
#             now = j
#             min_dist = distance[j]

#     visited[now] = 1

#     for v, cost in graph[now]:
#         if not visited[v] and cost < distance[v]:
#             distance[v] = cost

# print(sum(distance))