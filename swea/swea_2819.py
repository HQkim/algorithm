# swea 2819 격자판의 숫자 이어 붙이기
def f(x, y, tmp, cnt):
    if cnt == 6:            # 6번 이어붙이면 셋에 집어넣기
        num_set.add(tmp)
        return

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            f(nx, ny, tmp + graph[nx][ny], cnt+1)


T = int(input())
for tc in range(1, T+1):
    graph = [input().split() for _ in range(4)]

    num_set = set()
    for i in range(4):
        for j in range(4):
            f(i, j, graph[i][j], 0)     # 현재 row, 현재 column, 현재문자열, 이어붙인 횟수

    print(f'#{tc} {len(num_set)}')
