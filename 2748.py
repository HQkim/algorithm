# # bottom up
# import time

# n = int(input())
# start = time.time()

# i = 0
# pibo = []
# while True:
#     if i == 0:
#         pibo.append(0)
#     elif i == 1:
#         pibo.append(1)
#     else:
#         pibo.append(pibo[i-2]+pibo[i-1])
#     if i == n:
#         break
#     i += 1

# print(pibo[len(pibo)-1])
# print(time.time()-start)

# top down
import time
import sys

sys.setrecursionlimit(2000)  # 재귀 제한 완화하는 방법

n = int(input())

start = time.time()
d = [0] * 100200


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


print(fibo(n))
print(time.time()-start)
