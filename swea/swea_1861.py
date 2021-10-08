# swea 1861 정사각형 방

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    max_d = 0       # 최대 이동할 수 있는 방의 수
    max_list = []   # 이동거리가 최대인 출발하는 방 번호들의 배열

    for i in range(N):      # 모든 방들을 출발점으로
        for j in range(N):
            d = 1           # 처음 방문수는 1
            x = i           # 현재 행
            y = j           # 현재 열
            while True:
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:   # 상하좌우
                    nx = x + dx
                    ny = y + dy
                    is_movable = False                  # 더 움직일 수 있는지 체크하는 변수
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] == graph[x][y] + 1:
                            is_movable = True
                            x = nx
                            y = ny
                            d += 1
                            break

                if not is_movable:      # 움직일 수 없다면 while문 탈출
                    break

            if d > max_d:                       # 최대 방수보다 크다면 max_d 갱신 후 max_list 초기화 및 출발 방번호 추가
                max_d = d
                max_list.clear()
                max_list.append(graph[i][j])
            elif d == max_d:                    # 최대 방수와 같다면 기존 max_list에 방번호 추가
                max_list.append(graph[i][j])

    max_list.sort()

    print(f'#{tc} {max_list[0]} {max_d}')
