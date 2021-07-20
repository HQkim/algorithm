import math
import sys

m = 2*123456
array = [True for i in range(2*m+1)]
array[1] = 0

for i in range(2, int(math.sqrt(2*m)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= 2*m:
            array[i * j] = False
            j += 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if array[i]:
            count += 1
    print(count)
