N = int(input())
M = N
count = 0
a = 0

while(True):
    count += 1
    a = M//10 + M % 10
    M = 10*(M % 10) + a % 10
    if M == N:
        break


print(count)
