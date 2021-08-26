# swea 12712 파리퇴치3 -> 틀림 자꾸
def f(a, b, N, M):
    cross_num = arr[a][b]
    diagonal_num = arr[a][b]

    cross = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dist in range(1, M+1):
        for di, dj in cross:
            ni = a + di * dist
            nj = b + dj * dist
            if 0<=ni<N and 0<=nj<N:
                cross_num += arr[ni][nj]

    for dist in range(1, M+1):
        for di, dj in diagonal:
            ni = a + di * dist
            nj = b + dj * dist
            if 0<=ni<N and 0<=nj<N:
                diagonal_num += arr[ni][nj]

    return max(cross_num, diagonal_num)
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N):
        for j in range(N):
            num = f(i, j, N, M)
            if num > max_value:
                max_value = num
                print(i, j)


    print(f'#{tc} {max_value}')