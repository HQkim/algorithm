
# swea 1224 계산기3
'''
3+(4+5)*6+7
'''


def mid_to_postfix(expression):                     # 중위표기법 -> 후위표기법으로 변환하는 함수
    stack = []
    result = []

    for exp in expression:
        if exp == "(":
            stack.append(exp)
        elif exp == "*":
            if not stack:
                stack.append(exp)
            else:
                while stack:
                    a = stack[-1]
                    if a == "(" or a == "+":
                        break
                    else:
                        result.append(stack.pop())
                stack.append(exp)
        elif exp == "+":
            if not stack:
                stack.append(exp)
            else:
                while stack:
                    a = stack[-1]
                    if a == "(":
                        break
                    else:
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
    numbers = list(map(str, range(10)))

    for exp in expression:
        if exp in numbers:
            stack.append(exp)
        elif exp == "*":
            result = int(stack.pop()) * int(stack.pop())
            stack.append(result)
        else:
            result = int(stack.pop()) + int(stack.pop())
            stack.append(result)

    result = stack.pop()
    return result


T = 10
for tc in range(1, T+1):
    N = int(input())
    mid_expression = input()

    postfix_expression = mid_to_postfix(mid_expression)
    answer = calculate_postfix(postfix_expression)

    print(f'#{tc} {answer}')
