# 백준 10157 자리배정

import sys

input = sys.stdin.readline


def solution_a(C, R, K):
    if K > C * R:
        return 0, 0

    arry = [[0]*C for _ in range(R)]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    i, j = -1, 0
    number = 1

    d = 0
    while number <= K:
        ni, nj = i+di[d], j+dj[d]

        if 0 <= ni <= R-1 and 0 <= nj <= C-1 and arry[ni][nj] == 0:
            arry[ni][nj] = 1
            i, j = ni, nj
            number += 1
        else:
            d = (d+1) % 4

    return (j+1, i+1)


if __name__ == '__main__':
    C, R = map(int, input().split())
    K = int(input())
    x, y = solution_a(C, R, K)
    if x == 0 and y == 0:
        print(0)
    else:
        print(x, y)
