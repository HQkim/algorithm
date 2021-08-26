# swea 3499 퍼펙트 셔플

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input().split()

    print(f'#{tc}', end=' ')
    res = N % 2
    for i in range(N//2):
        print(f'{arr[i]}', end=' ')
        print(f'{arr[N//2+i+res]}', end=' ')
    if not res:
        print(f'{arr[N//2]}')