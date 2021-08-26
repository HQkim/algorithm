# swea 1226 미로1

def bfs(start, N):
    queue = [start]
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1

    is_possible = 0
    while queue:            # bfs
        now = queue.pop(0)

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:       # 상하좌우 탐색
            ni = now[0] + di
            nj = now[1] + dj
            if graph[ni][nj] != "1" and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))
                if ni == 13 and nj == 13:                       # 도착점에 도달하면 종료
                    is_possible = 1
                    break
        if is_possible:
            break

    return is_possible


T = 1
for _ in range(1, T+1):
    N = 16
    tc = int(input())
    graph = [input() for _ in range(N)]

    answer = bfs((1,1), N)
    print(f'#{tc} {answer}')
