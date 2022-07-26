# boj 2231 분해합

n = int(input())

answer = 0
min_start = max(1, n - len(str(n))*9)
for i in range(min_start, n):
    num = i + sum([int(j) for j in str(i)])
    if num == n:
        answer = i
        break

print(answer)
