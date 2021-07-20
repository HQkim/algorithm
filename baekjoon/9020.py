import math
import sys

m = 10000
array = [True for i in range(m+1)]
array[1] = 0

for i in range(2, int(math.sqrt(m)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= m:
            array[i * j] = False
            j += 1

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    i = int(n / 2)
    if array[i]:
        a = i
        b = i
    else:
        for j in range(i, 1, -1):
            b = n - j
            if array[j] and array[b]:
                break
        a = j

    print(a, b)
