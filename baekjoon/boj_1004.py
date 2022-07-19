# boj_1004 어린 왕자

import math
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        d1 = math.sqrt((cx-x1)**2 + (cy-y1)**2)
        d2 = math.sqrt((cx-x2)**2 + (cy-y2)**2)

        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            count += 1
    
    print(count)
