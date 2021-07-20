import sys

n, m = map(int, sys.stdin.readline().split())

a = [0]*m


def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()

        return
    for i in range(1, n+1):
        a[index] = i
        if index == 0 or (index >= 0 and i >= a[index-1]):
            go(index+1, n, m)


go(0, n, m)
