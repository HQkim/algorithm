# 백준 1934 최소공배수

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def solution():

    T = int(input())

    for _ in range(T):
        A, B = map(int, input().rstrip().split())
        gcd = find_greatest_common_divider(A, B)
        lcm = A * B // gcd
        print(lcm)

    return


def find_greatest_common_divider(A, B):
    if B == 0:
        return A
    else:
        return find_greatest_common_divider(B, A % B)


solution()
