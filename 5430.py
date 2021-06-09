# 백준 5430 AC

import sys
from collections import deque


def function_AC(commands, array):

    is_reverse = False

    front_position = 0
    back_position = len(array)

    for cmd in commands:
        if cmd == "R":
            is_reverse = not(is_reverse)
        elif cmd == "D":
            if front_position >= back_position:
                return "error"
            else:
                if is_reverse:
                    back_position -= 1
                else:
                    front_position += 1

    array = array[front_position:back_position]
    if is_reverse == True:
        array.reverse()
    return_value = "[" + ",".join(array) + "]"
    return return_value


def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        commands = input().strip()
        n = int(input().strip())
        array = input().strip()
        number_array = []
        if n != 0:
            number_array = array[1:-1].split(",")
        print(function_AC(commands, number_array))


main()

# 2021.06.08 지저분하게 한번 짬(직접 큐에서 pop시킴)
# 2021.06.09 코드 참조해서 새로운 로직(리스트에서 인덱스만 변경)
# 참조코드: https://www.acmicpc.net/source/11255731
