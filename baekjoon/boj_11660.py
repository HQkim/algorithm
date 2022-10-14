# BOJ 11660 구간 합 구하기 5

import sys


input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[0] * (N + 1)] + [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]
ans = []

# 행방향 누적합
for i in range(1, N + 1):
    for j in range(1, N + 1):
        graph[i][j] += graph[i][j - 1]

# 열방향 누적합
for i in range(1, N + 1):
    for j in range(1, N + 1):
        graph[j][i] += graph[j - 1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    part_sum = graph[x2][y2] + graph[x1 - 1][y1 - 1] - graph[x2][y1 - 1] - graph[x1 - 1][y2]
    ans.append(part_sum)

sys.stdout.write('\n'.join(map(str, ans)))
    
