# No.9663

import sys

n = int(sys.stdin.readline().rstrip())

check = [[False] * n] * n


def go(n, row, column, index, count):
    if index == n:
        count += 1
        return

    for i in range(column, n+1):
        if check[row][column] == False:
            for i in range(n):
