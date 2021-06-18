# 백준 11054번 가장 긴 바이토닉 부분 수열

import sys


def input_length_and_sequence():
    input = sys.stdin.readline
    length_of_sequence = int(input())
    sequence = list(map(int, input().rstrip().split()))
    return (length_of_sequence, sequence)


def length_of_longest_bitonic_subsequence(length_of_sequence, sequence):
    dp_forward = [1] * length_of_sequence
    for i in range(1, length_of_sequence):
        smaller_index_list = []
        for j in range(i-1, -1, -1):
            if sequence[i] > sequence[j]:
                smaller_index_list.append(j)

        if smaller_index_list:
            max_value = 0
            for k in smaller_index_list:
                if dp_forward[k] > max_value:
                    max_value = dp_forward[k]
            dp_forward[i] = max_value + 1

    dp_backward = [1] * length_of_sequence
    for i in range(length_of_sequence-2, -1, -1):
        smaller_index_list = []
        for j in range(i+1, length_of_sequence):
            if sequence[i] > sequence[j]:
                smaller_index_list.append(j)

        if smaller_index_list:
            max_value = 0
            for k in smaller_index_list:
                if dp_backward[k] > max_value:
                    max_value = dp_backward[k]
            dp_backward[i] = max_value + 1

    dp_total = [0] * length_of_sequence
    for i in range(length_of_sequence):
        dp_total[i] = dp_forward[i] + dp_backward[i] - 1

    return max(dp_total)


def main():
    length_of_sequence, sequence = input_length_and_sequence()
    answer = length_of_longest_bitonic_subsequence(
        length_of_sequence, sequence)
    print(answer)


main()
