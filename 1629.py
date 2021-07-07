# 백준 1629 곱셈

import sys

input = sys.stdin.readline


def solution():
    A, B, C = map(int, input().rstrip().split())

    def split_multiple(a, b):
        nonlocal C
        if b == 1:
            return a % C
        else:
            splited_number = split_multiple(a, b // 2)
            if b % 2 == 0:
                return splited_number * splited_number % C
            else:
                return splited_number * splited_number * a % C

    result = split_multiple(A, B)
    print(result)

    return


solution()
