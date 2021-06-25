# 백준 12015 가장 긴 증가하는 부분 수열 2

import sys
from bisect import bisect_left
input = sys.stdin.readline


def solution():

    n = int(input())
    array = list(map(int, input().rstrip().split()))
    lis_array = []
    answer = 0

    for num in array:
        if not lis_array:
            lis_array.append(num)
            answer += 1
            continue

        if lis_array[-1] < num:
            lis_array.append(num)
            answer += 1
        else:
            index = bisect_left(lis_array, num)
            lis_array[index] = num

    print(answer)

    return


solution()
