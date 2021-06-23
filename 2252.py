# 백준 2252 줄 세우기

import sys
from collections import deque

input = sys.stdin.readline


def solution():
    number_of_vertex, number_of_edge = map(int, input().rstrip().split())
    indegree = [0] * (number_of_vertex + 1)
    graph = [[] for _ in range(number_of_vertex + 1)]

    for _ in range(number_of_edge):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1

    def topology_sort():
        nonlocal number_of_vertex
        result = []
        queue = deque()

        for i in range(1, number_of_vertex + 1):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            now = queue.popleft()
            result.append(now)

            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return result

    result = topology_sort()
    for i in result:
        print(i, end=" ")

    return


solution()
