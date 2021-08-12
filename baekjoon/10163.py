# 백준 10163 색종이
import sys

input = sys.stdin.readline

N = int(input())
arry = [[0]*1001 for _ in range(1001)]
paper_count = [0] * (N+1)

for z in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(y, y+h):
        arry[i][x:x+w] = [z]*w

for i in range(1, N+1):
    count = 0
    for j in range(1001):
        count += arry[j].count(i)
    print(count)
