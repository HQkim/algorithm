# BOJ 1717 집합의 표현

import sys


def find_rep(x):
    if x == rep[x]:
        return x
    
    rep[x] = find_rep(rep[x])
    
    return rep[x]


def union(a, b):
    rep[find_rep(b)] = find_rep(a)


sys.setrecursionlimit(10**5)
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
rep = list(range(n+1))

for _ in range(m):
    act, a, b = map(int, input().split())
    if act == 0:
        if find_rep(a) < find_rep(b):
            union(a, b)
        else:
            union(b, a)
    else:
        rep_a = find_rep(a)
        rep_b = find_rep(b)
        if rep_a == rep_b:
            print('YES\n')
        else:
            print('NO\n')



# 10번째 줄에서 find_rep함수를 돌리면서 rep[x]를 갱신해 주는 작업이 시간 초과를 해결했다.