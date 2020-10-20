import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    num_list = list(range(n+1, 2*n+1))
    num = num_list[0]

    prime_count = 0
    while num <= num_list[-1]:
        count = 0
        for i in range(2, num+1):
            if num % i == 0 and i != num:
                count = 1
                break

        if count == 0 and num > 1:
            prime_count += 1
        num += 1
    print(prime_count)
