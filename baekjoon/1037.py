divisor_num = int(input())

if divisor_num == 1:
    divisor = int(input())
    print(divisor**2)
else:
    divisor_list = list(map(int, input().split()))
    divisor_list.sort()
    print(divisor_list[0] * divisor_list[-1])
