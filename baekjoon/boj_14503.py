# BOJ 14503 로봇 청소기
def robot(r, c, d):
    cnt = 0         # 청소한 칸의 개수

    while True:
        if not graph[r][c]:
            graph[r][c] = 2 # 1. 현재 방향을 청소
            cnt += 1

        is_possible = 0
        for i in range(1, 5):
            new_d = d - i   # 2-1. 왼쪽 방향 청소 X -> 회전한 다음 한칸 전진하고 1부터 진행
            new_d %= 4
            nr = r + directions[new_d][0]
            nc = c + directions[new_d][1]
            if not graph[nr][nc]:
                r, c, d = nr, nc, new_d
                is_possible = 1
                break

        if is_possible:
            continue

        new_d = d - 2
        nr = r + directions[new_d][0]
        nc = c + directions[new_d][1]
        if graph[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

    return cnt

N, M =  map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(robot(r, c, d))