# 2116 주사위 쌓기

import sys

input = sys.stdin.readline

n = int(input())
arry_all = [list(map(int, input().split())) for _ in range(n)]

match_dic = {"0": 5, "1": 3, "2": 4, "3": 1, "4": 2, "5": 0}

answer = 0
for i in range(1, 7):
    number = i
    total = 0
    for j in range(n):
        side = set(range(1, 7))
        arry = arry_all[j]

        ind = arry.index(number)
        side -= {number}

        counter_ind = match_dic[str(ind)]
        number = arry[counter_ind]
        side -= {number}

        total += max(side)

    if total > answer:
        answer = total

print(answer)
