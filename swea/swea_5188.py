# swea 5188 최소합
# Programmin/Advanced/완전 검색
def f(i, j, n, s):                  # 재귀적으로 합을 계산해 가는 함수
    global minV
    if i == n-1 and j == n-1:       # 맨오른쪽 아래에 도달 했을 때
        if s < minV:                # 현재합이 최소합보다 작으면 갱신
            minV = s
        return

    if s >= minV:                   # 이 부분이 없으면 시간초과 난다. 계산하다가 최소합보다 커지면 중단
        return

    for di, dj in [(0, 1), (1, 0)]:  # 오른쪽, 아래로 이동하는 경우에 대하여
        ni = i + di
        nj = j + dj
        if 0 <= ni <= n-1 and 0 <= nj <= n-1:   # 배열 안에 인덱스가 있는 경우
            f(ni, nj, n, s+graph[ni][nj])       # 다음 단계로 진행


T = int(input())
for tc in range(1, T+1):
    N = int(input())                                                # 배열의 크기
    graph = [list(map(int, input().split())) for _ in range(N)]     # 입력된 배열

    minV = 10 * N * N           # 최소합 정의
    f(0, 0, N, graph[0][0])     # 행, 열, 배열의 크기, 현재합

    print(f'#{tc} {minV}')
