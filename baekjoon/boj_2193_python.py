# boj 2193 이친수

N = int(input())

max_n = 90
dp = [0] * (max_n+1)

dp[1] = 1
dp[2] = 1
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])