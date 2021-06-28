# 백준 1806 부분합

import sys

input = sys.stdin.readline


def solution():
    length_of_array, sum_criteria = map(int, input().rstrip().split())
    array_of_numbers = list(map(int, input().rstrip().split()))

    start = 0
    end = 0

    min_length = 100001
    sum_of_subsequence = 0

    while end < length_of_array:

        sum_of_subsequence += array_of_numbers[end]

        if sum_of_subsequence >= sum_criteria:
            for i in range(start+1, end+1):
                sum_of_subsequence -= array_of_numbers[i-1]
                if sum_of_subsequence >= sum_criteria:
                    start = i
                else:
                    sum_of_subsequence += array_of_numbers[i-1]
                    break
            length_of_subsequence = end - start + 1
            if length_of_subsequence < min_length:
                min_length = length_of_subsequence

        end += 1

    if min_length == 100001:
        print(0)
    else:
        print(min_length)

    return


solution()
