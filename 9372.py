# 9372번 상근이의 여행

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().rstrip().split())

    for _ in range(M):
        input()
        # a, b = map(int, input().rstrip().split())
    print(N-1)

