# 2579번 계단 오르기

import sys

input = sys.stdin.readline

number_of_steps = int(input())

dp = []
for _ in range(number_of_steps):
    dp.append(int(input()))

for i in range(number_of_steps):
    if i == 0:
        dp[i] = [dp[i], dp[i]]
        continue
    if i == 1:
        dp[i] = [dp[i-1][0]+dp[i], dp[i]]
        continue
    dp[i] = [dp[i]+dp[i-1][1], dp[i]+max(dp[i-2])]

print(max(dp[-1]))