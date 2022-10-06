# BOJ 11052 카드 구매하기

N = int(input())
P = [0] + list(map(int, input().rstrip().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    pi = P[i]
    for j in range(1, N + 1):
        if j - i >= 0:
            dp[j] = max(dp[j], dp[j-i] + pi)

print(dp[N])