# programmers lv2 짝지어 제거하기

def solution(s):
    answer = 1
    stack = []

    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    if stack:
        answer = 0

    return answer

print(solution('baabaa'))