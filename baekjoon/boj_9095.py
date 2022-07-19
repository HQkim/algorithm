# boj 9095 1, 2, 3 더하기

import sys

input = sys.stdin.readline

T = int(input())
numbers = []
for _ in range(T):
    numbers.append(int(input()))

max_number = max(numbers)
dp = [0] * (max_number + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_number+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in numbers:
    print(dp[i])
