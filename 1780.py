# 백준 1780 종이의 개수

import sys

sys.setrecursionlimit(10**9)


def solution():
    number_of_numbers, array_of_numbers = input_numbers_in_paper()
    number_of_minus_papers = 0
    number_of_zero_papers = 0
    number_of_plus_papers = 0
    row_start_index = 0
    column_start_index = 0

    def count_number_of_papers(number_of_numbers, row_start_index, column_start_index):
        nonlocal number_of_minus_papers, number_of_zero_papers, number_of_plus_papers

        same_numbers_flag = True
        check_number_is_index_start = array_of_numbers[row_start_index][column_start_index]

        for i in range(row_start_index, row_start_index + number_of_numbers):
            for j in range(column_start_index, column_start_index + number_of_numbers):
                if array_of_numbers[i][j] != check_number_is_index_start:
                    same_numbers_flag = False
                    break
            if same_numbers_flag == False:
                break

        if same_numbers_flag == True:
            if check_number_is_index_start == -1:
                number_of_minus_papers += 1
            elif check_number_is_index_start == 0:
                number_of_zero_papers += 1
            else:
                number_of_plus_papers += 1
            return
        else:
            number_of_numbers //= 3
            for i in range(3):
                for j in range(3):
                    count_number_of_papers(number_of_numbers, row_start_index +
                                           i*number_of_numbers, column_start_index + j*number_of_numbers)
        return
    count_number_of_papers(
        number_of_numbers, row_start_index, column_start_index)
    print(number_of_minus_papers)
    print(number_of_zero_papers)
    print(number_of_plus_papers)


def input_numbers_in_paper():
    input = sys.stdin.readline
    number_of_numbers = int(input())
    array_of_numbers = [list(map(int, input().rstrip().split()))
                        for _ in range(number_of_numbers)]
    return (number_of_numbers, array_of_numbers)


solution()
