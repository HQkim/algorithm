# problem 1874 ---------미해결------------
import sys

n = int(sys.stdin.readline().rstrip())

stack = []
action = []
error = 1
for i in range(n):
    number = int(sys.stdin.readline().rstrip())
    if not stack:
        stack.append(number)
        action.append("+")
    else:
        temp = []
        while True:
            if number > stack[-1]:
                stack.append(number)
                action.append("+")
                break
            else:
                b = stack.pop()
                action.append("-")
                temp.append(b)
            if not stack:
                error = 1
                break
        for j in temp:
            stack.append(j)

if error:
    print("NO")
else:
    for i in action:
        print(i)
