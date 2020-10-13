import sys

n, m = map(int, sys.stdin.readline().split())

check = [False]*(n+1)
a = [0]*m


def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()

        return
    for i in range(1, n+1):
        if check[i]:
            continue
        check[i] = True
        a[index] = i
        go(index+1, n, m)
        check[i] = False


go(0, n, m)

# from itertools import permutations
# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)  # iter(tuple)
# for i in P:
#     print(' '.join(map(str, i)))  # tuple -> str
