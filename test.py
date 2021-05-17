import sys
M = 9**9
sys.setrecursionlimit(M)
a = [*map(int, sys.stdin.read().split()), M]


def f(i, u): p = a[i]; i += 1; i += p > a[i] and f(i, min(u, p)
                                                   )-i; i += u > a[i] and f(i, u)-i; print(p); return i


f(0, M)
