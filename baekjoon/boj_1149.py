# boj 1149 RGB거리

import sys

input = sys.stdin.readline

N = int(input())

rgb_costs = [list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        min_value = 1000*1000
        for k in range(3):
            if k != j:
                min_value = min(min_value, rgb_costs[i-1][k])
        rgb_costs[i][j] += min_value

print(min(rgb_costs[-1]))