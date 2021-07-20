import time

n = int(input())

start = time.time()

i = 2

for i in range(2, 10000001):
    if n == 1:
        break
    while True:
        if n % i != 0:
            break
        if n % i == 0:
            n //= i
            print(i)


print(time.time() - start)
