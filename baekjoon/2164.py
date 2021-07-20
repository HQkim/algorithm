# 2164번 카드2
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque([i for i in range(1, n+1)])

while True:
    ans = q.popleft()
    if not q:
        break
    p = q.popleft()
    q.append(p)

print(ans)
