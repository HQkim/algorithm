# 백준 1300 K번째 수

import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    k = int(input())

    start, end = 1, k

    while start <= end:
        mid = (start + end) // 2
        temp = 0

        for i in range(1, N + 1):
            temp += min(mid//i, N)

        if temp >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)

    return


solution()
