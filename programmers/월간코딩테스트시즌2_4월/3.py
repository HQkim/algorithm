
import sys
sys.setrecursionlimit(10000000)


def solution(a, edges):
    # 전체 합이 0이 아니면 바로 끝
    if sum(a):
        return -1

    answer = 0
    l = len(a)

    # graph 만들기
    graph = [[] for _ in range(l)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * l

    # 루트 노드(0)부터 dfs로 순회
    def dfs(node=0, parent=None):
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                dfs(neighbor, parent=node)

        if parent != None:
            nonlocal answer
            a[parent] += a[node]
            answer += abs(a[node])

    dfs()
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
