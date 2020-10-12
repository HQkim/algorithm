import sys

n = int(sys.stdin.readline())

member = [[i, sys.stdin.readline().strip().split()] for i in range(n)]

member_sort = sorted(
    sorted(member, key=lambda x: x[0]), key=lambda y: int(y[1][0]))

for i in range(n):
    print(member_sort[i][1][0], member_sort[i][1][1])
