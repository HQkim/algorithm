# 스택
# 10828번

import sys

n = int(sys.stdin.readline().rstrip())

stack = []
for i in range(n):
    order = sys.stdin.readline().rstrip()
    if "push" in order:
        order_list = order.split()
        stack.append(int(order_list[1]))
    elif order == "pop":
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if stack == []:
            print(1)
        else:
            print(0)
    else:
        if stack == []:
            print(-1)
        else:
            print(stack[-1])

# 소감
# input()과 sys.stdin.readline().rstrip()의 차이가 이렇게 큰 줄 몰랐다.
# input()으로 할 때는 바로 시간초과 나더니 sys...로 바꾸니 바로 정답.
