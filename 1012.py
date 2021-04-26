# 1012번

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().rstrip().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        graph[y][x] = 1

    q = deque([])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                answer += 1
                q.append((i,j))
                graph[i][j] = 0
                while q:
                    ni, nj = q.popleft()
                    for a in range(4):
                        bae_i = ni + di[a]
                        bae_j = nj + dj[a]
                        if bae_i < 0 or bae_i >= n or bae_j < 0 or bae_j >= m or graph[bae_i][bae_j] == 0:
                            continue
                        graph[bae_i][bae_j] = 0
                        q.append((bae_i, bae_j))

    print(answer)