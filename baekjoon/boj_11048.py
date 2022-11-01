# BOJ 11048 이동하기

import sys


input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[0] * (M + 1)]+ [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        graph[i][j] = graph[i][j] + max(graph[i - 1][j], graph[i][j - 1], graph[i - 1][j - 1])

print(graph[-1][-1])