# BOJ 10546 배부른 마라토너

import sys

input = sys.stdin.readline

N = int(input())
d = {}
for _ in range(N):
    name = input().strip()
    if d.get(name):
        d[name] += 1
    else: 
        d[name] = 1

for _ in range(N-1):
    name = input().strip()
    d[name] -= 1

for k, v in d.items():
    if v == 1:
        print(k)
        break