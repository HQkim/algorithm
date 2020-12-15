import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

a_list = [0]*10001
b_list = [0]*10001
a_list[1] = 1
b_list[1] = 1
a_max = 1
b_max = 1

for i in range(2, 10001):
    if a != 1:
        while True:
            if a % i == 0:
                a //= i
                a_list[i] += 1
            else:
                break
    if b != 1:
        while True:
            if b % i == 0:
                b //= i
                b_list[i] += 1
            else:
                break
    if a == 1:
        a_max = i
    if b == 1:
        b_max = i
    if a == 1 and b == 1:
        break

num_max = max([a_max, b_max])

gcf, lcm = 1, 1
for i in range(1, num_max + 1):
    if a_list[i]*b_list[i] != 0:
        gcf_fact = min([a_list[i], b_list[i]])
        gcf *= i**gcf_fact
    if a_list[i] != 0 or b_list[i] !=0:
        lcm_fact = max([a_list[i], b_list[i]])
        lcm *= i**lcm_fact
        
print(gcf)
print(lcm)

        
