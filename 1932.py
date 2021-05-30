# 백준 1932번 정수삼각형

import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    numbers = []
    for _ in range(n):
        line = map(int, input().rstrip().split())
        numbers.append(list(line))

    for i in range(1, n):

        for j in range(i+1):
            if j == 0:
                numbers[i][j] += numbers[i-1][0]
                continue
            if j == i:
                numbers[i][j] += numbers[i-1][-1]
            else:
                numbers[i][j] += max(numbers[i-1][j-1], numbers[i-1][j])
    print(max(numbers[-1]))


solution()
