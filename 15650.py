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
        if index == 0:
            a[index] = i
            go(index+1, n, m)
        if index > 0 and i > a[index-1]:
            a[index] = i
            go(index+1, n, m)
        check[i] = False


go(0, n, m)
