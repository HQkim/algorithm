# BOJ 6588 골드바흐의 추측
import sys

input = sys.stdin.readline
print = sys.stdout.write

limit = 10**6
nums = [1] * (limit + 1)

for i in range(2, limit+1):
    if nums[i]:
        for j in range(i*2, limit+1, i):
            nums[j] = 0

while True:
    n = int(input())
    if n == 0:
        break

    x, y = 3, n-3
    is_p = False
    while x <= y:

        if nums[x] and nums[y]:
            is_p = True
            break
        else:
            x += 2
            y -= 2

    if is_p:
        print(f'{n} = {x} + {y}\n')
    else:
        print("Goldbach's conjecture is wrong.\n")