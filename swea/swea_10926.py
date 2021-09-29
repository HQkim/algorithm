# swea 10926 7-bit 10진수

T = int(input())
for tc in range(1, T+1):
    number_binary = input()                 # 전체 70자리 2진수 숫자
    print(f'#{tc}', end=" ")
    for i in range(10):
        n_b = number_binary[i*7:(i+1)*7]    # 7자리씩 끊은 후에
        n_b = '0b' + n_b                    # 변환을 위해 '0b'붙여주기
        print(f'{int(n_b, 2)}', end=" ")    # 10진수로 변환해서 출력
    print()
