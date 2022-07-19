# boj 15829 Hashing

import sys

input = sys.stdin.readline

L = int(input())
a = input()

ord_a = ord('a')
r = 31
M = 1234567891

h = 0
for i in range(L):
    h += (ord(a[i]) - ord_a + 1) * r**i

h %= M

print(h)
