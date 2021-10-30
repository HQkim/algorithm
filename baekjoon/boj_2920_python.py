# boj 2920 음계

import sys

input = sys.stdin.readline

nodes = list(map(int, input().split()))

is_ascending = True
is_descending = True
for i in range(7):
    if nodes[i] < nodes[i+1]:
        is_descending = False
    if nodes[i] > nodes[i+1]:
        is_ascending = False

if not is_ascending and not is_descending:
    print('mixed')
elif is_ascending:
    print('ascending')
else:
    print('descending')
