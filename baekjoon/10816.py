# 10816번 숫자 카드 2

import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))

n_dict = dict()
for i in n_list:
    if n_dict.get(i) == None:
        n_dict[i] = 1
    else:
        n_dict[i] += 1

m = int(input())
m_list = list(map(int, input().rstrip().split()))

for i in m_list:
    if n_dict.get(i) == None:
        print(0, end=" ")
    else:
        print(n_dict[i], end=" ")
