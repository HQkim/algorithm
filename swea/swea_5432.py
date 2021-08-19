# swea 5432 쇠막대기 자르기

T = int(input())
for tc in range(1, T+1):
    braket = input()

    count = 0
    stack = []
    for i in range(len(braket)):
        b = braket[i]
        if b == "(":                # "("인 경우에는 스택에 삽입
            stack.append(b)
        else:                       # ")"인 경우
            if braket[i-1] == "(":  # 이전 원소가 "("이면 레이저. 스택에서 하나 빼고 남은 수만큼 개수 증가
                stack.pop()
                count += len(stack)
            else:                   # 이전 원소가 ")"이면 막대기 하나 스택에서 빼고 개수 증가
                count += 1
                stack.pop()

    print(f'#{tc} {count}')
