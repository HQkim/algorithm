import sys

n = int(sys.stdin.readline())

num = [0]*10001
print(num)
for i in range(n):
    x = int(sys.stdin.readline())
    num[x] += 1

for i in range(1, 10001):
    if num[i] != 0:
        for c in range(num[i]):
            print(i)
