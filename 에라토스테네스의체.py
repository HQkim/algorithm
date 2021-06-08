import sys
import math

input = sys.stdin.readline

start, end = map(int, input().rstrip().split())

array = [True for i in range(1000001)]
array[1] = 0

for i in range(2, int(math.sqrt(end)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= end:
            array[i * j] = False
            j += 1

for i in range(start, end + 1):
    if array[i]:
        print(i)
