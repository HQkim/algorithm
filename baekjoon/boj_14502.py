# BOJ 14502 연구소
from itertools import combinations
from collections import deque


def bfs(N, M, virus_number, wall_number):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    for vp in virus_points:
        q.append(vp)
        visited[vp[0]][vp[1]] = 1

    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + direc[i][0]
            ny = y + direc[i][1]
            if 0<=nx<N and 0<=ny<M and not graph[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    
    result = N*M - (cnt + virus_number + wall_number + 3)
    return result

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direc =[(1, 0), (-1, 0), (0, 1), (0, -1)]

wall_points = []
virus_points = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall_points.append((i, j))
        if graph[i][j] == 2:
            virus_points.append((i, j))
virus_number = len(wall_points)
wall_number = len(virus_points)


points = []
for i in range(N):
    for j in range(M):
        if (i, j) not in wall_points and (i, j) not in virus_points:
            points.append((i, j))

points_combis = list(combinations(points, 3))

cnt_max = 0
for three_points in points_combis:
    for p in three_points:
        graph[p[0]][p[1]] = 1
    
    cnt = bfs(N, M, virus_number, wall_number)
    cnt_max = max(cnt_max, cnt)

    for p in three_points:
        graph[p[0]][p[1]] = 0

print(cnt_max)