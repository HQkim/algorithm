import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

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

count = 0
for i in num_list:
    if i in primenumber:
        count += 1

print(count)
