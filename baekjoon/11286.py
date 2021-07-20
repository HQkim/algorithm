# 11286번

import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            sys.stdout.write(str(0)+"\n")
        else:
            temp = []
            while True:
                if not q:
                    break
                t_abs, t = map(int, heapq.heappop(q))
                if not temp:
                    temp.append((t_abs, t))
                else:
                    if temp[-1][0] != t_abs:
                        heapq.heappush(q,(t_abs,t))
                        break
                    else:
                        temp.append((t_abs, t))
            
            temp.sort(key = lambda x: x[0])
            temp_queue = deque(temp)
            p = temp_queue.popleft()[1]
            sys.stdout.write(str(p)+"\n")
            for i in temp_queue:
                heapq.heappush(q, i)

# 나는 우선순위 큐 하나에 다 넣고 중복되는거 다 뽑아서 했는데 그냥 양수 우선순위큐와 음수 우선순위큐 두개를 돌리면 훨씬 빠름