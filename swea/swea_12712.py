# swea 12712 파리퇴치3 -> 틀림 자꾸 -> 문제 잘 읽자. M =3 일때 주위 두칸만 체크
def f(i, j, N, M):
    cross_dp = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    diag_dp = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

    cross_num = graph[i][j]
    diag_num = graph[i][j]

    for x in range(1, M):
        for dp in cross_dp:
            ni = i + dp[0]*x
            nj = j + dp[1]*x
            if 0<=ni<N and 0<=nj<N:
                cross_num += graph[ni][nj]

    for x in range(1, M):
        for dp in diag_dp:
            ni = i + dp[0]*x
            nj = j + dp[1]*x
            if 0<=ni<N and 0<=nj<N:
                diag_num += graph[ni][nj]

    return max(cross_num, diag_num)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N):
        for j in range(N):
            num = f(i, j, N, M)
            if num > max_value:
                max_value = num

    print(f'#{tc} {max_value}')