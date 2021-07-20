import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, M = map(int, input().rstrip().split())

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    queue = deque()

    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    def topology_sort():

        while queue:
            now = queue.popleft()
            print(now, end=" ")

            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return
    topology_sort()

    return


solution()
