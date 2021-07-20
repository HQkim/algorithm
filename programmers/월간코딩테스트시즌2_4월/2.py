from collections import deque


def solution(s):
    answer = 0

    s = deque(s)

    for i in range(len(s)):
        if i != 0:
            s.append(s.popleft())

        stack = []
        error = 0

        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            elif i == ")":
                if not ("(" in stack):
                    error = 1
                    break
                else:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        error = 1
                        break
            elif i == "]":
                if not ("[" in stack):
                    error = 1
                    break
                else:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        error = 1
                        break
            elif i == "}":
                if not ("{" in stack):
                    error = 1
                    break
                else:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        error = 1
                        break
        if not stack and error == 0:
            answer += 1
    return answer


print(solution("}]()[{"))
