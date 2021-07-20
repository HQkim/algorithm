import sys
import time

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

past = time.time()

num_list = list(range(m, n+1))
num_max = max(num_list)

num = 0
primenumber = []

while num < num_max:
    num += 1
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        primenumber.append(num)

print(time.time() - past)

# for i in primenumber:
#     print(i)


# prime = []
# for i in num_list:
#     if i in primenumber:
#         prime.append(i)

# if len(prime) == 0:
#     print(-1)
# else:
#     print(sum(prime))
#     print(min(prime))
