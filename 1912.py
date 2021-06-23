# 백준 1912 연속합

import sys

input = sys.stdin.readline


def solution():
    number_of_numbers = int(input())
    array_of_numbers = list(map(int, input().rstrip().split()))

    dp = [0] * number_of_numbers
    dp[0] = array_of_numbers[0]

    for i in range(1, number_of_numbers):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + array_of_numbers[i]
        else:
            dp[i] = array_of_numbers[i]

    print(max(dp))

    return


solution()
