# 11279번

import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())

    if x > 0:
      heapq.heappush(q, -x)
    else:
        if not q:
            sys.stdout.write(str(0)+"\n")
        else:
            sys.stdout.write(str(-heapq.heappop(q))+"\n")