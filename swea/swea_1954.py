# swea 1954 달팽이
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arry = [[0]*N for _ in range(N)]    # 달팽이 배열

    di = [0, 1, 0, -1]      # k값(인덱스)에 따라 i(행)값에 더해줄 값들
    dj = [1, 0, -1, 0]      # k값(인덱스)에 따라 j(행)값에 더해줄 값들

    number = 1              # 시작 숫자
    i, j = 0, -1            # 시작 행,열
    k = 0                   # 방향(0이면 오른쪽, 1이면 아래, 2면 위, 3이면 위쪽)
    while number <= N*N:
        ni, nj = i+di[k], j+dj[k]   # 새로운 행,열값
        # 새로운 행,열 값이 정해진 범위 안에 있고 그때의 달팽이 값이 처음 간 곳일 떄
        if 0 <= ni <= N-1 and 0 <= nj <= N-1 and arry[ni][nj] == 0:
            arry[ni][nj] = number
            i, j = ni, nj
            number += 1
        else:  # 방향 바꿔주기
            k = (k+1) % 4

    print(f'#{tc}')
    for i in range(N):
        print(*arry[i], end=" ")
        print()
