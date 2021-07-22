# 백준 1244 스위치 켜고 끄기

import sys

input = sys.stdin.readline


def solution():
    number_of_switches = int(input())
    switch_state = list(map(int, input().split()))
    number_of_students = int(input())
    students = [0] * number_of_students
    for i in range(number_of_students):
        students[i] = list(map(int, input().split()))

    for s in students:
        if s[0] == 1:
            number = s[1]
            for i in range(number_of_switches):
                if (i+1) % number == 0:
                    if switch_state[i] == 1:
                        switch_state[i] = 0
                    else:
                        switch_state[i] = 1

        else:
            pivot_number = s[1] - 1
            diff = 1
            start_number = pivot_number - diff
            end_number = pivot_number + diff

            if not(start_number >= 0 and end_number <= number_of_switches - 1):
                if switch_state[pivot_number] == 1:
                    switch_state[pivot_number] = 0
                else:
                    switch_state[pivot_number] = 1
                continue
            while start_number >= 0 and end_number <= number_of_switches - 1:
                if switch_state[start_number] != switch_state[end_number]:
                    diff -= 1
                    break
                if start_number == 0 or end_number == number_of_switches - 1:
                    break
                diff += 1
                start_number -= 1
                end_number += 1

            start = pivot_number - diff
            end = pivot_number + diff
            for i in range(start, end + 1):
                if switch_state[i] == 1:
                    switch_state[i] = 0
                else:
                    switch_state[i] = 1

    for i in range(number_of_switches):
        if i == 0:
            print(switch_state[i], end=" ")
        elif i % 20 == 19:
            print(switch_state[i])
        else:
            print(switch_state[i], end=" ")

    return


if __name__ == "__main__":
    solution()
