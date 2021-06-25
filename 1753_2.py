import sys
import heapq

input = sys.stdin.readline
INF = int(10e9)


def solution():
    v, e = map(int, input().rstrip().split())
    start = int(input())
    distance = [INF] * (v + 1)
    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for i in range(e):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))

    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distance[start] = 0

        while queue:
            cost, now = heapq.heappop(queue)

            if visited[now] == 1:
                continue

            visited[now] = 1

            for edge in graph[now]:
                dist = cost + edge[1]
                vertex = edge[0]

                if dist < distance[vertex]:
                    distance[vertex] = dist
                    heapq.heappush(queue, (dist, vertex))

    dijkstra(start)
    for i in range(1, v + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])

    return


solution()
