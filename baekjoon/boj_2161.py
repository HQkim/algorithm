# boj 2161 카드1

from collections import deque

N = int(input())
arr = deque([i for i in range(1, N+1)])

while len(arr)>1:
    print(arr.popleft(), end=" ")
    arr.append(arr.popleft())

print(arr.popleft())

