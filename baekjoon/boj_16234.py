# BOJ 16234 인구 이동
import sys
from collections import deque


def solution():
    day = 0
    visited = [[-1] * N for _ in range(N)]
    countries = deque([(x, y) for x in range(N) for y in range(x%2, N, 2)]) # 체크할 국가들 (처음에 격자 형태의 국가들만 체크하기)
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]                               # 상, 하, 좌, 우

    while countries:
        q = deque()
        for _ in range(len(countries)):
            x, y = countries.popleft()                                      # 처음 시작 국가
            if visited[x][y] == day:
                continue
            visited[x][y] = day
            group = [(x, y)]
            group_cnt = graph[x][y]
            q.append((x, y))

            # BFS
            while q:
                r, c = q.popleft()
                num = graph[r][c]
                for dr, dc in move:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] != day and L <= abs(num - graph[nr][nc]) <= R: 
                        visited[nr][nc] = day
                        group.append((nr, nc))
                        group_cnt += graph[nr][nc]
                        q.append((nr, nc))
            
            # 국가가 2개 이상이라면 이동시키고, 체크할 국가에 추가하기
            if len(group) > 1:                                            
                group_mean_cnt = group_cnt // len(group)
                for r, c in group:
                    graph[r][c] = group_mean_cnt
                    countries.append((r, c))

        if countries:
            day += 1

    return day


if __name__ == '__main__':
    input = sys.stdin.readline
    N, L, R = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    answer = solution()
    print(answer)