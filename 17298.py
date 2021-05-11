# 17298번 오큰수 몇번 시도끝에 타인의 코드 참조

import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * n
val = 0
stack = []

for i in range(n - 2, -1, -1):
    tmp = numbers.pop()
    stack.append(tmp)
    if numbers[i] < tmp:
        val = tmp
    if numbers[i] >= val:
        while stack:
            val = stack.pop()
            if numbers[i] < val:
                answer[i] = val
                stack.append(val)
                break
    else:
        answer[i] = val
print(*answer)

