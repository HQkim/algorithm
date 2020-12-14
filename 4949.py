# 4949번

import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    stack = []
    error = 0

    if sentence == ".":
        break

    try:
        for i in sentence:
            if i == "(":
                stack.append(i)
            elif i == "[":
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
        if not stack and error == 0:
            print("yes")
        else:
            print("no")

    except:
        print("no")
