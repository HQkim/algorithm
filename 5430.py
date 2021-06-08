# 백준 5430 AC

import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

answer_list = []
for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    if n == 0:
        input()
        number_array = []
    else:
        number_array = deque(input().strip()[1:-1].split(","))

    error_flag = False
    popleft_flag = True
    for cmd in p:
        if cmd == "D" and not(number_array):
            answer_list.append("error")
            error_flag = True
            break
        if cmd == "D" and popleft_flag:
            number_array.popleft()
            continue
        if cmd == "D" and not(popleft_flag):
            number_array.pop()
            continue
        if cmd == "R":
            popleft_flag = not(popleft_flag)

    if not(popleft_flag):
        number_array.reverse()

    if not error_flag:
        length_array = len(number_array)
        if length_array == 0:
            answer_list.append("[]")
        elif length_array == 1:
            answer_list.append("[{}]".format(number_array[0]))
        else:
            answer = ""
            for i in range(length_array):
                if i == 0:
                    answer = "".join([answer, '[{}'.format(number_array[i])])
                    continue
                if i == length_array - 1:
                    answer = "".join([answer, ",{}]".format(number_array[i])])
                    continue
                answer = "".join([answer, ",{}".format(number_array[i])])
            answer_list.append(answer)

for ans in answer_list:
    print(ans)
