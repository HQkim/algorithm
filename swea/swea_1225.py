# swea 1225 암호생성기
T = 10
for _ in range(1, T+1):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1                       # 처음 빼는 숫자는 1
    while True:
        num = queue.pop(0)      # 맨 앞자리 숫자 pop
        num -= i                # i만큼 빼기
        if num <= 0:            # 0보다 작거나 같으면 0을 마지막에 더하기
            queue.append(0)
            break
        queue.append(num)
        i += 1
        i %= 5
        if i == 0:              # 5의 배수인 경우는 5를 빼주기
            i = 5

    print(f'#{tc}', *queue)