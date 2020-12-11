import math
import sys
import time

m, n = map(int, sys.stdin.readline().rstrip().split())

past = time.time()

array = [True for i in range(10000001)]
array[1] = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

print(time.time() - past)

for i in range(m, n + 1):
    if array[i]:
        print(i)

# 주석: 에로토스테네스의 체를 쓰면 약 100배 빨라짐..
