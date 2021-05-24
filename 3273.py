# 3273번 두 수의 합

import sys

input = sys.stdin.readline

n = int(input())
arry = list(map(int, input().rstrip().split()))
x = int(input())

arry.sort()

start = 0
end = n-1

answer = 0
while start < end:
    value = arry[start] + arry[end]
    if value == x:
        answer += 1
        start += 1
        continue
    if value > x:
        end -= 1
        continue
    if value < x:
        start += 1

print(answer)
