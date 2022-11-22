# BOJ 11727 2×n 타일링 2

n = int(input())
dp = [0] * (n+1)

if n > 0:
    dp[1] = 1
if n > 1:
    dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[-1]%10007)