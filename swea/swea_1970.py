# swea 1970 쉬운 거스름돈

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_count = [0] * 8

    for i in range(len(money_list)):
        div = N // money_list[i]
        N = N - money_list[i] * div
        money_count[i] = div
        if N == 0:
            break

    print(f'#{tc}')
    print(*money_count)
