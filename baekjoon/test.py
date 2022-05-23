# boj 1011 Fly me to the Alpha Centauri

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().rstrip().split())
    print(x, y)
