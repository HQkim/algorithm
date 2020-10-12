import sys

n = int(sys.stdin.readline())

if n == 1:
    anw = 666
else:
    num = 666
    c = 1
    while True:
        num += 1
        if "666" in str(num):
            c += 1
            if c == n:
                anw = num
                break

print(anw)
