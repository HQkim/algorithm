# 백준 2920 음계

import sys

input = sys.stdin.readline


def solution():

    array_of_notes = list(map(int, input().rstrip().split()))
    ascending_flag = False
    descending_flag = False

    if array_of_notes[0] == 1:
        ascending_flag = True
    elif array_of_notes[0] == 8:
        descending_flag = True

    if ascending_flag:
        for i in range(1, 8):
            if array_of_notes[i] != array_of_notes[i-1] + 1:
                ascending_flag = False
                break

    if descending_flag:
        for i in range(1, 8):
            if array_of_notes[i] != array_of_notes[i-1] - 1:
                descending_flag = False
                break

    if ascending_flag:
        print("ascending")
        return

    if descending_flag:
        print("descending")
        return

    print("mixed")

    return


solution()
