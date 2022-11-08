# BOJ 6064 카잉 달력

import sys


def count_year(M, N, x, y):
    limit = M*N

    while x <= limit:
        if (x - y) % N == 0:
            return x
        x += M 

    return -1


if __name__ == '__main__':
    sys = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().rstrip().split())
        answer = count_year(M, N, x, y)
        print(answer)
