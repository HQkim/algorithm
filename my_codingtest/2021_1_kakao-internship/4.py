import copy
import sys

sys.setrecursionlimit(10000)


def solution(n, start, end, roads, traps):
    INF = int(10e9)  # 길이 없는 것을 표시
    traps = set(traps)  # trap list를 set로 변환
    visited = [0] * (n+1)

    # graph 초기값 설정
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for road in roads:
        graph[road[0]][road[1]] = min(graph[road[0]][road[1]], road[2])

    answer_list = []
    cost = 0

    def dfs(now, end, graph, cost):
        visited[now] += 1
        if now == end:  # 목적지 도달
            answer_list.append(cost)
            return
        if now in traps:  # now가 trap이면 길 거꾸로
            for i in range(1, n+1):
                graph[i][now], graph[now][i] = graph[now][i], graph[i][now]

        graph_temp = copy.deepcopy(graph)
        for des in range(1, n+1):
            if graph[now][des] != INF and (visited[des] == 0 or (visited[des] == 1 and des in traps)):
                dfs(des, end, graph_temp, cost + graph[now][des])
        return

    dfs(start, end, graph, cost)

    return min(answer_list)


solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
