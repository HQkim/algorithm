# prob 1904

import sys

n = int(sys.stdin.readline().rstrip())

temp1 = 1
temp2 = 2

if n == 1:
    print(temp1)
elif n ==2:
    print(temp2)
else:
    for i in range(2, n):
        temp = (temp1 + temp2) % 15746
        temp1 = temp2
        temp2 = temp

    print(temp)
