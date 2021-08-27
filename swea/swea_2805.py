# swea 2805 농작물 수확하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    N_2 = N // 2
    count = 0
    for i in range(N):
        for j in range(N):
            if (i+j) >= N_2 and (i+j) <= N+N_2-1 and abs(i-j) <= N_2:
                count += int(arr[i][j])
    print(f'#{tc} {count}')