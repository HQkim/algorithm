# swea 4366 정식이의 은행업무

T = int(input())
for tc in range(1, T+1):
    binary = input()        # 입력받는 2진법 문자열
    ternary = input()       # 입력받는 3진법 문자열

    binary_init_num = int(binary, 2)    # 입력받은 2진법 수의 처음 10진법 값
    ternary_init_num = int(ternary, 3)  # 입력받은 3진법 수의 처음 10진법 값

    binary_list = list(map(int, binary))    # 2진법 수를 리스트로 저장
    ternary_list = list(map(int, ternary))   # 3진법 수를 리스트로 저장

    binary_list_rev = binary_list[::-1]     # 거꾸로 저장
    ternary_list_rev = ternary_list[::-1]

    binary_num_set = set()                  # 2진법 수를 한자리씩 바꿔가며 나오는 수를 중복 없이 저장
    for i in range(len(binary_list_rev)):
        init = binary_list_rev[i]
        for j in range(2):
            num = binary_init_num
            if j != init:
                num = num - init*(2**i) + j*(2**i)
                binary_num_set.add(num)

    ternary_num_set = set()                 # 3진법 수를 한자리씩 바꿔가며 나오는 수를 중복 없이 저장
    for i in range(len(ternary_list_rev)):
        init = ternary_list_rev[i]
        for j in range(3):
            num = ternary_init_num
            if j != init:
                num = num - init*(3**i) + j*(3**i)
                ternary_num_set.add(num)

    common_num_set = binary_num_set & ternary_num_set   # 2진법과 3진법 수에서 나온 값들의 교집합

    print(f'#{tc} {common_num_set.pop()}')
