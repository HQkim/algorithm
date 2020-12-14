# problem 18258

import sys
from collections import deque

dq = deque([])

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order[:2] == "pu":
        order_list = order.split()
        dq.append(int(order_list[1]))
    elif order == "pop":
        if dq:
            pop = dq.popleft()
            print(pop)
        else:
            print(-1)
    elif order == "size":
        print(len(dq))
    elif order == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif order == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)
