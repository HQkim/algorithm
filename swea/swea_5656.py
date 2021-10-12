# swea 5656 벽돌 깨기
import copy


def f(col, arr, cnt, n):
    global min_num

    # 맨위 벽돌 찾기
    row = -1                    # row가 -1이면 벽돌이 없다는 의미
    for i in range(H):
        if arr[i][col]:
            row = i
            break

    if row != -1:               # 열에 벽돌이 있다면 폭발처리한 후에 벽돌 떨어뜨리기
        # 폭발 처리
        visited = [[0]*W for _ in range(H)]
        stack = []
        stack.append((row, col))
        visited[row][col] = 1

        while stack:
            r, c = stack.pop()
            splash_range = arr[r][c]
            for s in range(splash_range):
                if s == 0:
                    arr[r][c] = 0
                else:
                    for dr, dc in [(0, s), (s, 0), (0, -s), (-s, 0)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            stack.append((nr, nc))

        # 벽돌 떨어뜨리기
        for x in range(W):
            col_list = []
            for y in range(H-1, -1, -1):
                if arr[y][x]:
                    col_list.append(arr[y][x])
            length = len(col_list)
            col_list += [0]*(H-length)
            col_list.reverse()

            for y in range(H):
                arr[y][x] = col_list[y]

    if cnt == n:                # 구슬을 다 쐈으면 최소 벽돌수 갱신
        num = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    num += 1
        min_num = min(min_num, num)
        return

    for x in range(W):
        f(x, copy.deepcopy(arr), cnt+1, n)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]

    min_num = W*H           # 최소 벽돌 수

    for j in range(W):
        f(j, copy.deepcopy(graph), 1, N)

    print(f'#{tc} {min_num}')
