# 백준 2605 줄 세우기

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    numbers = list(range(1, n+1))

    stack = []
    for i in range(n):
        temp = []
        for j in range(arr[i]):
            temp.append(stack.pop())

        stack.append(i+1)
        while temp:
            stack.append(temp.pop())

    print(*stack)
