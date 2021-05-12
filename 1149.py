# 1149번 RGB거리

import sys

input = sys.stdin.readline

n = int(input())
dp = []

for _ in range(n):
    a, b, c = map(int, input().rstrip().split())
    dp.append([a,b,c])

def cost_min(dp, n):
    for now in range(1, n):
        for i in range(3):
            stack = []
            for j in range(3):
                if i != j:
                    stack.append(dp[now-1][j])
            dp[now][i] = dp[now][i] +min(stack)
    return min(dp[n-1])

print(cost_min(dp, n))
    































# 동적 계획법