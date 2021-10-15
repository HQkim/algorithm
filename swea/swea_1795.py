# swea 1795 인수의 생일 파티
import heapq


def dijkstra(start, graph):     # 다익스트라 알고리즘
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in range(1, N+1):
            if graph[now][i] != INF:
                cost = graph[now][i] + dist
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

    return distance


INF = int(10e9)
T = int(input())
for tc in range(1, T+1):
    # 정점의 개수, 간선의 개수, 생일파티 정점
    N, M, X = map(int, input().split())

    graph_org = [[INF]*(N+1) for _ in range(N+1)]       # 처음 받은 간선 정보
    # 처음 받은 간선 정보를 transpose한 것
    graph_trans = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph_org[x][y] = c

    for i in range(N+1):
        for j in range(N+1):
            graph_trans[j][i] = graph_org[i][j]

    distance_backward = dijkstra(X, graph_org)          # 생일정점에서 돌아올 때 걸리는 거리
    distance_forward = dijkstra(X, graph_trans)         # 생일정점으로 가는데 걸리는 거리

    max_dist = 0
    for i in range(1, N+1):
        total = distance_forward[i] + distance_backward[i]
        max_dist = max(max_dist, total)

    print(f'#{tc} {max_dist}')
