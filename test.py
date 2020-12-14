from collections import deque
import time

n = 1000000

a = list(range(0, n))

start = time.time()

dq = deque([])
# dq = []

for i in a:
    dq.append(i)

for i in range(n):
    dq.popleft()

print(time.time() - start)
