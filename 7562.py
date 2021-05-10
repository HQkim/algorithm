# 7562번
# 나이트의 이동

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

pos = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

n_list = []
for _ in range(T):
    l = int(input())
    visited = [[False]*l for _ in range(l)]
    x0, y0 = map(int, input().rstrip().split())
    x1, y1 = map(int, input().rstrip().split())

    q = deque([(x0, y0, 0)])
    visited[x0][y0] = True

    while q:
        x, y, n = q.popleft()
        if x == x1 and y == y1:
            break
        
        Flag = False
        for p in pos:
            x_n = x + p[0]
            y_n = y + p[1]
            if 0<=x_n<l and 0<=y_n<l and visited[x_n][y_n] == False:
                if x_n == x1 and y_n == y1:
                    Flag = True
                    break
                q.append((x_n, y_n, n+1))
                visited[x_n][y_n] = True
                
        if Flag == True:
            n += 1
            break
        
    n_list.append(n)

for i in n_list:
    print(i)