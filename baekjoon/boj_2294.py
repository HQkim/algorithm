# BOJ 2294 동전 2
import sys

input = sys.stdin.readline

INF = int(10e9)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [INF] * (k+1)
dp[0] = 0 

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
