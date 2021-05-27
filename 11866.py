# 백준 11866번 요세푸스문제0

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

queue = deque([i for i in range(1, N + 1)])

answer = []
while queue:
    for i in range(K-1):
        left = queue.popleft()
        queue.append(left)
    answer.append(queue.popleft())

print("<", end="")
for i in range(N):
    if i == N-1:
        print("{}>".format(answer[i]))
        break
    print("{}, ".format(answer[i]), end="")
