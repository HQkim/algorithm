# 백준 12865 평범한 배낭

import sys

input = sys.stdin.readline


def solution():
    number_of_stuff, maximum_weight = map(int, input().rstrip().split())

    stuff = [[0, 0]]
    kanpsack = [[0 for _ in range(maximum_weight + 1)]
                for _ in range(number_of_stuff + 1)]

    for _ in range(number_of_stuff):
        stuff.append(list(map(int, input().rstrip().split())))

    for i in range(1, number_of_stuff + 1):
        weight = stuff[i][0]
        value = stuff[i][1]
        for j in range(1, maximum_weight + 1):
            if j < weight:
                kanpsack[i][j] = kanpsack[i - 1][j]
            else:
                kanpsack[i][j] = max(value + kanpsack[i - 1]
                                     [j - weight], kanpsack[i - 1][j])

    print(kanpsack[number_of_stuff][maximum_weight])

    return


solution()
