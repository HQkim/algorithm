# BOJ 2167 2차원 배열의 합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    part_sum = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(part_sum)


# 워낙 유명한 dp 및 구간합 문제이기는 하나
# 이게 브론즈문제인지는 모르겠다.
# 오랜만에 푸니깐 시간이 좀 걸렸다.