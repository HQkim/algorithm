# 백준 2565 전깃줄

import sys


def solution():
    number_of_connections, line_connections = input_line_connections()
    line_connections.sort()
    number_of_minimum_lines_cut = calculate_minimum_lines_cut(
        number_of_connections, line_connections)

    print(number_of_minimum_lines_cut)
    return


def input_line_connections():
    input = sys.stdin.readline
    number_of_connections = int(input())
    line_connections = []
    for _ in range(number_of_connections):
        line_connections.append(tuple(map(int, input().rstrip().split())))
    return (number_of_connections, line_connections)


def calculate_minimum_lines_cut(number_of_connections, line_connections):
    second_post_numbers = []
    for row in line_connections:
        second_post_numbers.append(row[1])

    # 결국 increasing 하는 부분수열을 찾는 문제였다!
    number_of_lines_not_cut = length_of_longest_increasing_subsequence(
        number_of_connections, second_post_numbers)

    number_of_lines_cut = number_of_connections - number_of_lines_not_cut

    return number_of_lines_cut


def length_of_longest_increasing_subsequence(length_of_sequence, sequence):
    dp = [1] * length_of_sequence
    for i in range(1, length_of_sequence):
        smaller_index_list = []
        for j in range(i-1, -1, -1):
            if sequence[i] > sequence[j]:
                smaller_index_list.append(j)

        if smaller_index_list:
            max_value = 0
            for k in smaller_index_list:
                if dp[k] > max_value:
                    max_value = dp[k]
            dp[i] = max_value + 1
    return max(dp)


solution()
