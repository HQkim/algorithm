# boj 2206 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

visited = [[0]*M for _ in range(N)]  # 방문표시 배열
visited[0][0] = 1
queue = deque()                     # 큐 생성
queue.append((0, 0, 0, 1))          # 행, 열, 벽부순 여부, 이동거리
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

min_dist = -1       # 최단 경로 -1로 설정
while queue:
    row, col, is_break, dist = queue.popleft()

    if row == N-1 and col == M-1:   # 목표 지점에 도달한 경우
        min_dist = dist
        break

    for dr, dc in directions:
        nr = row + dr
        nc = col + dc
        # 범위를 벗어나지 않고 방문하지 않았을 떄
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if not is_break:
                if graph[nr][nc] == 0:                      # 통로일 경우
                    visited[nr][nc] = 1
                    queue.append((nr, nc, is_break, dist+1))
                else:   # 벽이고 부술 수 있는 경우
                    visited[nr][nc] = 1
                    queue.append((nr, nc, 1, dist+1))
            else:
                if graph[nr][nc] == 0:                      # 통로일 경우
                    visited[nr][nc] = 1
                    queue.append((nr, nc, is_break, dist+1))

print(min_dist)
