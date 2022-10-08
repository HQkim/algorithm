# BOJ 11057 오르막 수

N = int(input())

dp = [0] * 10
dp[0] = 1

for i in range(N):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp)%10007)