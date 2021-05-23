# 9461번 파도반 수열

import sys

input = sys.stdin.readline

dp = [0]*101
for i in range(1,4):
    dp[i] = 1
dp[4], dp[5] = 2, 2
for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])