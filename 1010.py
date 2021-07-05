# 백준 1010 다리 놓기

import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    
    for _ in range(T):
        N, M = map(int, input().rstrip().split())
        result = factorial(M) // (factorial(M-N) * factorial(N))
        print(result)

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

solution()