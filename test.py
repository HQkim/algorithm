
# swea 1224 계산기3
'''
3+(4+5)*6+7
'''


def mid_to_postfix(expression):                     # 중위표기법 -> 후위표기법으로 변환하는 함수
    stack = []
    result = []

    for exp in expression:
        if exp in in_comming_priority:
            if not stack:
                stack.append(exp)
            else:
                while stack:
                    a = stack[-1]
                    priority_a = in_stack_priority[a]
                    priority_exp = in_comming_priority[exp]
                    if priority_exp > priority_a:
                        break
                    result.append(stack.pop())
                stack.append(exp)
        elif exp == ")":
            while stack:
                a = stack[-1]
                if a == "(":
                    stack.pop()
                    break
                else:
                    result.append(stack.pop())
        else:
            result.append(exp)

    if stack:
        while stack:
            result.append(stack.pop())

    return result


def calculate_postfix(expression):                          # 후위 표기법을 계산하는 함수
    stack = []

    for exp in expression:
        if exp == "*":
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif exp == "+":
            stack.append(int(stack.pop()) + int(stack.pop()))
        else:
            stack.append(exp)

    result = stack.pop()
    return result


T = 10
for tc in range(1, T+1):
    N = int(input())
    mid_expression = input()

    in_comming_priority = {"(": 3, "*": 2, "+": 1}
    in_stack_priority = {"(": 0, "*": 2, "+": 1}

    postfix_expression = mid_to_postfix(mid_expression)
    answer = calculate_postfix(postfix_expression)

    print(f'#{tc} {answer}')
