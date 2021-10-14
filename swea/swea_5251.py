# swea 5251 최소 이동 거리
# programming advanced/그래프의 최소 비용문제
import heapq


def dijkstra(start):                # 다익스트라 알고리즘
    q = []
    heapq.heappush(q, (0, start))   # 최소힙에 (거리0, 출발지)를 넣는다
    distance[start] = 0             # 출발지의 거리는 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:        # 이미 처리된적 있는 지점이면 continue
            continue

        for i in graph[now]:            # 처리된 적 없으면 연결된 지점들에 대해
            cost = dist + i[1]
            if cost < distance[i[0]]:   # 현재 지점에서 연결된 지점까지의 경로의 길이가 기존 거리보다 짧으면 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(10e9)
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())    # 마지막 연결지점 번호, 도로의 개수
    V = N + 1                           # 연결지점의 개수

    start = 0                           # 시작 지점

    graph = [[] for _ in range(V)]

    distance = [INF] * V                # 최단 거리 테이블을 모두 무한으로 초기화

    for _ in range(E):
        s, e, w = map(int, input().split())     # 구간 시작, 구간 끝, 구간 거리
        graph[s].append((e, w))

    dijkstra(start)

    print(f'#{tc} {distance[N]}')
