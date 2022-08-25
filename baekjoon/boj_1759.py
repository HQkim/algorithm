# BOJ 1759 암호 만들기

from itertools import combinations
import sys

input = sys.stdin.readline
print = sys.stdout.write

vowels = 'aeiou'
L, C = map(int, input().split())
arr = input().rstrip().split()
arr.sort()
combis = combinations(arr, L)

for combi in combis:
    cnt_v = 0
    cnt_c = 0
    for c in combi:
        if c in vowels:
            cnt_v += 1
        else:
            cnt_c += 1
    if cnt_v and cnt_c > 1:
        print(f"{''.join(combi)}\n")