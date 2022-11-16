# BOJ 2493 탑
import sys


input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rstrip().split()))    
stack = []
answer = [0] * (N)

for i in range(N):
    num = arr[i]
    if not stack:
        stack.append((i, num))
    else:
        while stack:
            if num < stack[-1][1]:
                answer[i] = stack[-1][0] + 1
                stack.append((i, num))
                break
            else:
                stack.pop()
        if not stack:
            stack.append((i, num))

print(" ".join(map(str, answer)))