import time
import math

now = time.time()

# n = 1212210202001
n = 21171114

a = [0, 0] + [1] * (n-1)
primes = []
print(int(math.sqrt(n))+1)
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = 0

print(time.time() - now)

print(f"{time.time()-now:.5f}")

# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# print(f"{time.time()-now:.5f}")
# print(is_prime)
