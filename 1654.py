# 백준 1654번 랜선 자르기

import sys


def solution():
    number_of_lanline, number_of_needed_lanline, array_of_lanlines = input_lanline_information()
    maximum_lanline_length = calculate_maximum_lanline_length(
        number_of_lanline, number_of_needed_lanline, array_of_lanlines)
    print(maximum_lanline_length)
    return


def input_lanline_information():
    input = sys.stdin.readline
    n, k = map(int, input().rstrip().split())
    array = []
    for _ in range(n):
        array.append(int(input()))
    return (n, k, array)


def calculate_maximum_lanline_length(number_of_lanline, number_of_needed_lanline, array_of_lanlines):
    start = 1
    end = max(array_of_lanlines)

    answer = []
    while start <= end:
        calculated_number_of_lanline = 0
        mid = (start + end) // 2

        for i in range(number_of_lanline):
            calculated_number_of_lanline += array_of_lanlines[i] // mid

        if calculated_number_of_lanline < number_of_needed_lanline:
            end = mid - 1
        else:
            start = mid + 1
            answer.append(mid)

    return max(answer)


solution()
