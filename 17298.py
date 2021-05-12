# 17298번 오큰수 몇번 시도끝에 타인의 코드 참조 / 한번 더 보고 조금 더 이해

import sys

input = sys.stdin.readline

n =int(input())
arry = list(map(int, input().rstrip().split()))

nge = [-1]*n
stack = []

for i in range(n-2, -1, -1):
    right = arry[i+1]
    stack.append(right)

    if arry[i] < right:
        nge[i] = right
        continue
    
    while stack:
        num = stack.pop()
        if arry[i] < num:
            nge[i] = num
            stack.append(num)
            break

print(*nge)
