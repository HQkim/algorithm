# BOJ 2798 블랙잭

from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
combis = combinations(arr, 3)

d_min = int(10e9)
s_min = 0
for comb in combis:
    s = sum(comb)
    if s > M:
        continue
    
    d = M - s
    if d < d_min:
        d_min = d
        s_min = s

print(s_min)