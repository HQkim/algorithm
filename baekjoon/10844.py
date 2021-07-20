# 백준 10844번 쉬운계단수

import sys
from collections import deque


def main():
    input = sys.stdin.readline
    n = int(input())
    stairs = [[0] * 10 for _ in range(n + 1)]

    stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, n + 1):
        stairs[i][0] = stairs[i - 1][1]
        stairs[i][9] = stairs[i - 1][8]

        for j in range(1, 9):
            stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]

    print(sum(stairs[n]) % 1000000000)
main()

# 2021.06.12 https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98 참조
