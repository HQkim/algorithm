# BOJ 4949 균형잡힌 세상

import sys
input = sys.stdin.readline

while 1:
    word = input().rstrip()
    if word == '.':
        break

    stack = []
    is_sym = True
    for w in word:
        if w == '(':
            stack.append(w)
        elif w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_sym = False
                break
        elif w == '[':
            stack.append(w)
        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_sym = False
                break            

    if not stack and is_sym == True:
        print('yes')
    else:
        print('no')
