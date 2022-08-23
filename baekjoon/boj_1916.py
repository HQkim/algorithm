# BOJ 1916 최소비용 구하기
import heapq
import sys

input = sys.stdin.readline
INF = int(10e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

# 그래프에 간선 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

# 다익스트라 알고리즘
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:        # 이미 방문한적 있다면 continue
        continue

    if now == end:                  # 도착지에 도달했다면 종료
        break

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:   # 경로가 단축될 경우 heap에 추가
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[end])