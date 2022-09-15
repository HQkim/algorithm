# programmers 2020_카카오인턴십

from itertools import permutations
import copy

def solution(expression):
    answer = 0

    # 1. 문자열 split해서 리스트로 만들고, 사용된 연산자 찾기
    exp_list, used_operators = split_exp_and_find_operators(expression)

    # 2. 연산자 우선순위 만들기
    operator_priorities = make_operator_priority(used_operators)
    print(operator_priorities)

    # 3. 우선순위별 상금 계산하기
    for operator_priority in operator_priorities:
        money = calculate(exp_list, operator_priority)
        answer = max(answer, money)

    return answer


def split_exp_and_find_operators(expression):
    exp_list = []
    operators = ['+', '-', '*']
    op_set = set()
    num = ''

    for e in expression:
        if e in operators:
            op_set.add(e)
            exp_list.append(num)
            exp_list.append(e)
            num = ''
        else:
            num += e
    if num:
        exp_list.append(num)

    return exp_list, list(operators)


def make_operator_priority(operators):
    operator_list = list(permutations(operators, len(operators)))

    return operator_list


def calculate(exp_list, operators):
    exp = copy.deepcopy(exp_list)
    for operator in operators:
        for i in range(len(exp)):
            if exp[i] == operator:
                j = 1
                while True:
                    if exp[i - j] != 'skip':
                        num1 = exp[i - j]
                        exp[i - j] = 'skip'
                        break
                    j += 1

                j = 1
                while True:
                    if exp[i + j] != 'skip':
                        num2 = exp[i + j]
                        exp[i + j] = 'skip'
                        break
                    j += 1

                if operator == '+':
                    exp[i] = int(num1) + int(num2)
                elif operator == '-':
                    exp[i] = int(num1) - int(num2)
                else:
                    exp[i] = int(num1) * int(num2)

    for i in range(len(exp)):
        if exp[i] != 'skip':
            money = exp[i]

    return abs(money)


solution("100-200*300-500+20")
solution("50*6-3*2")