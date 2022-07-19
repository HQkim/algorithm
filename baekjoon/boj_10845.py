# boj 10845 큐

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    cmd = input().strip()
    if cmd[:4] == "push":
        num = int(cmd[5:])
        queue.append(num)
    elif cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
