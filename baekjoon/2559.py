# 백준 2559 수열

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arry = list(map(int, input().split()))

for i in range(1, N):       # 누적합 구하고
    arry[i] += arry[i-1]

max_sum = -int(10e9)
for i in range(K-1, N):
    if i == K-1:
        part_sum = arry[i]
    else:
        part_sum = arry[i] - arry[i-K]

    if part_sum > max_sum:
        max_sum = part_sum

print(max_sum)
