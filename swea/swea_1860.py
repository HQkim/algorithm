# swea 1860 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    max_time = max(arr)             # 계산할 최대 시간
    need = [0] * (max_time+1)       # 매 시간 필요한 붕어빵 개수를 저장
    for i in arr:
        need[i] += 1
    for i in range(1, max_time+1):
        need[i] += need[i-1]

    supply = [0] * (max_time+1)     # 매 시간 만들어져 있는 붕어빵의 개수 저장
    for i in range(max_time+1):
        supply[i] = (i // M) * K
    
    is_possible = "Possible"
    for i in range(max_time+1):
        if need[i] > supply[i]:
            is_possible = "Impossible"
            break
    
    print(f'#{tc} {is_possible}')

