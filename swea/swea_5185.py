# swea 5185 이진수
# Programming Advanced 시작하기

T = int(input())
for tc in range(1, T+1):
    # 16진수 딕셔너리 만들기
    hex_dict = {}
    for i in range(10):
        hex_dict[str(i)] = i

    A_ord = ord('A')
    num = 10
    for i in range(A_ord, A_ord+6):
        hex_dict[chr(i)] = num
        num += 1

    print(f'#{tc}', end=' ')

    # 16진수 -> 2진수
    N, num_hex = input().split()
    for h in num_hex:
        num_deci = hex_dict[h]              # 16진수 -> 10진수
        num_bin = bin(num_deci)             # 10진수 -> 2진수
        length = len(num_bin[2:])
        left = 4 - length
        num_bin = '0'*left + num_bin[2:]    # 출력형태 맞추기
        print(f'{num_bin}', end='')

    print()
