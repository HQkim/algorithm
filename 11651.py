import sys
from operator import itemgetter

n = int(sys.stdin.readline())

cord = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cord = sorted(cord, key=itemgetter(1, 0))

for i in cord:
    print(i[0], i[1])
