# 백전 2635 수 이어가기
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    max_length = 1
    max_length_list = [n]

    for i in range(1, n+1):
        number_list = [n, i]

        while True:
            number = number_list[-2] - number_list[-1]
            if number >= 0:
                number_list.append(number)
            else:
                break

        length_list = len(number_list)
        
        if length_list > max_length:
            max_length = length_list
            max_length_list = number_list

    print(max_length)
    print(*max_length_list, end=" ")

    return


solution()
