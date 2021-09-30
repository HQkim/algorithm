# swea 10726 이진수 표현

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    M_bin = bin(M)[2:]
    length = len(M_bin)
    ans = 'ON'

    if length < N:
        ans = 'OFF'
    else:
        for i in range(length-1, length-N-1, -1):
            if M_bin[i] == '0':
                ans = 'OFF'
                break

    print(f'#{tc} {ans}')
