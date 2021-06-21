# 백준 1707 이분 그래프

import sys
from collections import deque

input = sys.stdin.readline


def solution():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        number_of_vertex, graph = input_number_of_vertex_and_graph()
        answer = is_bipartite_graph(number_of_vertex, graph)
        print(answer)
    return


def input_number_of_vertex_and_graph():
    number_of_vertex, number_of_edge = map(int, input().rstrip().split())
    graph = [[] for _ in range(number_of_vertex + 1)]
    for _ in range(number_of_edge):
        edge_1, edge_2 = map(int, input().rstrip().split())
        graph[edge_1].append(edge_2)
        graph[edge_2].append(edge_1)
    return (number_of_vertex, graph)


def is_bipartite_graph(number_of_vertex, graph):
    vertex_color = [0] * (number_of_vertex + 1)
    flag_stop = False
    for i in range(1, number_of_vertex + 1):
        if flag_stop:
            break
        if vertex_color[i] > 0:
            continue

        vertex_color[i] = 1
        queue = deque([i])

        while queue and not flag_stop:
            q = queue.popleft()
            c = 3 - vertex_color[q]

            for j in graph[q]:
                if vertex_color[j] == 0:
                    vertex_color[j] = c
                    queue.append(j)
                elif vertex_color[j] == vertex_color[q]:
                    flag_stop = True
                    break
    return "YES" if not flag_stop else "NO"


solution()
