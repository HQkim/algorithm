# 백준 2470 두 용액

import sys

input = sys.stdin.readline
INF = int(10e10)


def solution():
    number_of_liquids = int(input())
    array_of_liquids = list(map(int, input().rstrip().split()))
    array_of_liquids.sort()

    start = 0
    end = number_of_liquids - 1
    min_acidity_absolute = int(INF)

    min_acidity_absolute_index = [(INF, INF)]
    while start < end:
        mixed_acidity = array_of_liquids[start] + array_of_liquids[end]
        mixed_acidity_absolute = abs(mixed_acidity)
        if mixed_acidity_absolute < min_acidity_absolute:
            min_acidity_absolute = mixed_acidity_absolute
            min_acidity_absolute_index[0] = (start, end)
        if mixed_acidity_absolute == 0:
            break
        if mixed_acidity > 0:
            end -= 1
        else:
            start += 1

    print(array_of_liquids[min_acidity_absolute_index[0][0]],
          array_of_liquids[min_acidity_absolute_index[0][1]])

    return


solution()
