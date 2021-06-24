# 백준 1766 문제집

import sys
import heapq

input = sys.stdin.readline


def solution():
    number_of_node, number_of_edge = map(int, input().rstrip().split())
    indegree = [0] * (number_of_node + 1)
    graph = [[] for _ in range(number_of_node + 1)]

    for _ in range(number_of_edge):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1

    def topology_sort():
        nonlocal number_of_node
        result = []
        queue = []

        for i in range(1, number_of_node + 1):
            if indegree[i] == 0:
                heapq.heappush(queue, i)

        while queue:
            now = heapq.heappop(queue)
            result.append(now)
            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    heapq.heappush(queue, i)
        return result

    result = topology_sort()
    for i in result:
        print(i, end=" ")

    return


solution()
