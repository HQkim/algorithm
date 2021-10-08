# swea 1953 탈주범 검거

from collections import deque

# 방향에 따라 행,열에 더할 수를 저장. 0,1,2,3은 순서대로 우,하,좌,상을 의미한다.
move_direction = {
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1),
    '3': (-1, 0)
}

# 전 터널에서 각 방향(위와 같은 기준)으로 움직였을때 그 방향에 연결될 수 있는 터널 종류
in_dict = {
    '0': [1, 3, 6, 7],
    '1': [1, 2, 4, 7],
    '2': [1, 3, 4, 5],
    '3': [1, 2, 5, 6],
}

# 현 터널에서 움직일 수 있는 방향(위와 같은 기준)
out_dict = {
    '1': [0, 1, 2, 3],
    '2': [1, 3],
    '3': [0, 2],
    '4': [0, 3],
    '5': [0, 1],
    '6': [1, 2],
    '7': [2, 3],
}


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]     # 터널 그래프
    # 터널에 방문했는지 나타내기 위한 배열
    visited = [[0]*M for _ in range(N)]

    queue = deque()
    queue.append((R, C, L-1))
    visited[R][C] = 1

    while queue:
        row, col, t = queue.popleft()
        if t:       # 시간이 남아 있다면
            shape = graph[row][col]     # 현재 터널의 모양번호
            possible_directions = out_dict.get(
                str(shape))  # 현재 터널에서 갈 수 있는 방향 목록
            for direction in possible_directions:
                dr, dc = move_direction.get(str(direction))
                nr = row + dr   # 다음 이동할 위치의 행
                nc = col + dc   # 다음 이동할 위치의 열
                # 다음 이동할 위치가 그래프 내에 있고 방문하지 않은 경우
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    # 다음 방문할 터널의 모양 번호
                    n_shape = graph[nr][nc]
                    # 방문할 터널이 현재 터널과 연결되어 있다면 큐에 추가
                    if n_shape in in_dict.get(str(direction)):
                        queue.append((nr, nc, t-1))
                        visited[nr][nc] = 1

    ans = 0
    for i in range(N):
        ans += sum(visited[i])

    print(f'#{tc} {ans}')
