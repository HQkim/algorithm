import sys
from itertools import permutations

input = sys.stdin.readline


def solution():
    number_of_numbers = int(input())
    array_of_numbers = list(map(int, input().rstrip().split()))
    operators = list(map(int, input().rstrip().split()))

    array_of_operators = []
    for i in range(4):
        number_of_this_operator = operators[i]
        array_of_operators += [i] * number_of_this_operator

    permutations_of_operators = set(permutations(
        array_of_operators, number_of_numbers-1))

    max_value = -int(10e9)
    min_value = int(10e9)

    for operator_list in permutations_of_operators:
        result = array_of_numbers[0]

        for i in range(number_of_numbers - 1):
            op = operator_list[i]
            if op == 0:
                result += array_of_numbers[i+1]
            elif op == 1:
                result -= array_of_numbers[i+1]
            elif op == 2:
                result *= array_of_numbers[i+1]
            else:
                if result > 0:
                    result //= array_of_numbers[i+1]
                else:
                    result = -(abs(result) // array_of_numbers[i+1])

        if result > max_value:
            max_value = result
        if result < min_value:
            min_value = result

    print(max_value)
    print(min_value)


solution()
