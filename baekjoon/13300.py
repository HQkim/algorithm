import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arry = [[0, 0] for _ in range(6)]

for _ in range(n):
    s, grade = map(int, input().split())
    arry[grade-1][s] += 1

count = 0
for i in arry:
    for j in range(2):
        div = i[j]//k
        res = i[j] % k
        if res:
            div += 1
        count += div

print(count)
