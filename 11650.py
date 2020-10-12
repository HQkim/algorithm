import sys

n = int(sys.stdin.readline())

cord = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cord.sort()

for i in cord:
    print(i[0], i[1])
