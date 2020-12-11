import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    test = sys.stdin.readline().rstrip()

    stack = []
    try:
        for j in test:
            if j == "(":
                stack.append(j)
            else:
                stack.pop()
        if not stack:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")
