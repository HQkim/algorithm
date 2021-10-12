# swea 2105 디저트 카페

def f(row, col, cnt, is_move):
    global start_row, start_col, N, max_num
    dr, dc = direction[cnt]                             # 직진시 행과 열에 더해줄 값

    # 마지막 방향(3)이라면
    if cnt == 3:
        if row == start_row and col == start_col:           # 만약 현재 행과 열이 시작점이라면 최대 디저트수 갱신
            max_num = max(max_num, len(cafes))

        nr = row + dr                                   # 다음 위치로 이동
        nc = col + dc
        if 0 <= nr < N and 0 <= nc < N:                 # 다음 위치가 범위 안이라면
            if nr == start_row and nc == start_col:         # 시작점과 동일해진다면 최대 디저트수 갱신
                max_num = max(max_num, len(cafes))
            elif graph[nr][nc] not in cafes:                # 시작점과 동일하지 않고 투어한 디저트와 겹치지 않으면
                cafes.append(graph[nr][nc])                 # 다음 디저트로 진행
                f(nr, nc, cnt, 1)
                cafes.pop()
        return

    # 0,1,2 방향일 때 직진
    nr = row + dr
    nc = col + dc
    # 바뀐 행과 열이 범위 안이고 투어한 디저트와 겹치지 않으면 진행
    if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] not in cafes:
        cafes.append(graph[nr][nc])
        f(nr, nc, cnt, 1)
        cafes.pop()

    # 처음 출발점이 아니라 한번이라도 움직였다면 방향 바꿔서 진행해보기
    if is_move:
        nr = row + direction[cnt+1][0]
        nc = col + direction[cnt+1][1]
        if 0 <= nr < N and 0 <= nc < N:                 # 방향을 바꿔서 한칸 갔을 때 범위 안일 때
            if nr == start_row and nc == start_col:         # 만약 도착점이라면 투어한 디저트 검사 X
                f(nr, nc, cnt+1, 1)
            elif graph[nr][nc] not in cafes:                # 도착점이 아니면 투어한 디저트 검사후 진행
                cafes.append(graph[nr][nc])
                f(nr, nc, cnt+1, 1)
                cafes.pop()


# 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위 방향에 따라 행과 열 증가
direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    max_num = -1        # 초기 최대 디저트수를 -1로 설정
    for i in range(N):
        for j in range(N):
            start_row, start_col = i, j     # 시작 행과 열을 기록
            cafes = [graph[i][j]]           # 현재까지 투어한 디저트의 번호 기록
            f(i, j, 0, 0)                   # 현재 행, 현재 열, 방향, 한번이라도 움직였는지 여부

    print(f'#{tc} {max_num}')
