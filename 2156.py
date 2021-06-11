# 백준 2156번 포두주 시식

import sys


def maximum_wine(array):
    array_length = len(array)
    dp = [0 for _ in range(array_length)]
    dp[0] = array[0]
    for i in range(1, array_length):
        if i == 1:
            dp[i] = array[0] + array[1]
        elif i == 2:
            dp[i] = max(array[2]+array[0], array[2]+array[1], dp[1])
        else:
            dp[i] = max(array[i]+dp[i-2], array[i]+array[i-1]+dp[i-3], dp[i-1])
    return max(dp)


def main():
    input = sys.stdin.readline
    n = int(input())
    wine = [int(input()) for _ in range(n)]
    answer = maximum_wine(wine)
    print(answer)


main()
