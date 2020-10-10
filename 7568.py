import sys

n = int(sys.stdin.readline())

p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

rank = []
for i in range(n):
    count = 1
    for j in range(n):
        if i != j:
            if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
                count += 1
    rank.append(count)

for i in rank:
    print(i, end=" ")
