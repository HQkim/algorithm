# 백준 2475 검증수

import sys

input = sys.stdin.readline


def solution():

    array = list(map(int, input().rstrip().split()))

    total = 0
    for i in range(5):
        total += array[i]**2

    print(total % 10)

    return


solution()
