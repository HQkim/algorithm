# problem 1874

import sys
from collections import deque

input = sys.stdin.readline

stack = []
n = int(input())
numbers = deque([i for i in range(1, n+1)])

sequence = []
for i in range(n):
    x = int(input())
    sequence.append(x)

answer = []
num_max = 0
for i in sequence:
    target = i
    if target > num_max:
        while numbers:
            p = numbers.popleft()
            stack.append(p)
            answer.append("+")
            num_max = p
            if p == target:
                break
    if stack[-1] == target:
        stack.pop()
        answer.append("-")
        continue
    else:
        answer.clear()
        answer.append("NO")
        break

for i in answer:
    print(i)
