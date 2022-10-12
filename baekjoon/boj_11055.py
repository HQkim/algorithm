# BOJ 11055 가장 큰 증가 부분 수열

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1001

for a in arr:
    dp[a] = max(dp[:a]) + a

print(max(dp))

