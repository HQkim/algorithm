# 백준 1504 특정한 최단 경로

import sys
import heapq

input = sys.stdin.readline
INF = int(10e9)


def solution():
    number_of_vertex, number_of_edge = map(int, input().rstrip().split())
    graph = input_graph_info(number_of_vertex, number_of_edge)
    must_pass_vertex_1, must_pass_vertex_2 = map(int, input().rstrip().split())

    def dijkstra(start):
        nonlocal number_of_vertex
        distance = [INF] * (number_of_vertex + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        return distance

    distance_start = dijkstra(1)
    distance_vertex_1 = dijkstra(must_pass_vertex_1)
    distance_vertex_2 = dijkstra(must_pass_vertex_2)

    distance_pass_vertex_1_and_vertex_2 = distance_start[must_pass_vertex_1] + \
        distance_vertex_1[must_pass_vertex_2] + \
        distance_vertex_2[number_of_vertex]
    distnace_pass_vertex_2_and_vertex_1 = distance_start[must_pass_vertex_2] + \
        distance_vertex_2[must_pass_vertex_1] + \
        distance_vertex_1[number_of_vertex]

    if distance_pass_vertex_1_and_vertex_2 <= distnace_pass_vertex_2_and_vertex_1:
        answer = distance_pass_vertex_1_and_vertex_2
    else:
        answer = distnace_pass_vertex_2_and_vertex_1

    if answer >= int(10e9):
        answer = -1

    print(answer)
    return


def input_graph_info(number_of_vertex, number_of_edge):
    graph = [[] for _ in range(number_of_vertex + 1)]

    for _ in range(number_of_edge):
        v1, v2, d = map(int, input().split())
        graph[v1].append((v2, d))
        graph[v2].append((v1, d))

    return graph


solution()
