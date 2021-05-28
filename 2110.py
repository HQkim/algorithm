# 백준 2110.py 공유기설치

import sys
import time

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
past = time.time()
arry = [0] * N
for i in range(N):
    arry[i] = int(input())
arry.sort()

start = 1
end = arry[-1] - arry[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    old = arry[0]
    count = 1

    for i in range(1, len(arry)):
        if arry[i] >= old + mid:
            count += 1
            old = arry[i]

    print(start, end, mid, count)

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)
