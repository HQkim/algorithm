# 1927번

import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(q, x)
    else:
        if not q:
            sys.stdout.write(str(0)+"\n")
        else:
            sys.stdout.write(str(heapq.heappop(q))+"\n")