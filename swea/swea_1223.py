# swea 1223 계산기2
def step1(expression):                          # 후위표기식 계산식을 리스트로 반환하는 함수
    stack = []                                  # 연산자를 담은 스택
    result = []                                 # 결과값을 담을 리스트
    numbers = list(map(str, range(10)))

    for exp in expression:
        if exp in numbers:                      # 숫자일 경우 결과 리스트에 바로 담기
            result.append(exp)
        elif exp == "*":                        # 곱하기일 경우 연산자 스택에 담기
            stack.append(exp)
        else:                                   # 더하기일 경우
            if not stack:                       # 연산자 스택이 비어 있으면 담고
                stack.append(exp)
            else:                               # 연산자 스택이 차있으면
                while stack:
                    result.append(stack.pop())  # 연산자 스택을 모두 결과 리스트에 담고
                stack.append(exp)               # 빈 연산자 스택에 더하기 담기
    while stack:                                # 연산자 스택이 차있다면 마지막에는 모두 결과 리스트에 담기
        result.append(stack.pop())
    return result


def step2(expression):                          # 후위표기식 계산식을 계산하는 함수
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
    expression = input()                        # 중위표기식 계산식

    postfix_expression = step1(expression)      # 후위표기식 계산식
    answer = step2(postfix_expression)          # 후위표기식 계산식 계산

    print(f'#{tc} {answer}')
