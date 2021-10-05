# swea 5201 컨테이너
# Programmin/Advanced/탐욕 알고리즘

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())       # 컨테이너 수 N, 트럭 수 M
    w = list(map(int, input().split()))    # 화물의 무게
    t = list(map(int, input().split()))    # 트럭의 적재용량

    w.sort(reverse=True)                   # 화물의 무게 내림차순 정렬
    t.sort(reverse=True)                   # 트럭의 적재용량 내림차순 정렬

    w_i = 0                                 # 현재 화물의 무게 인덱스
    t_i = 0                                 # 현재 트럭의 적재용량 인덱스
    ans = 0                                 # 화물의 총 중량
    while True:
        if w_i >= N or t_i >= M:            # 인덱스를 벗어나면 종료
            break

        if t[t_i] >= w[w_i]:                # 트럭의 적재용량 >= 화물의 무게라면
            ans += w[w_i]                   # 화물의 총 중량에 더해주기
            w_i += 1                        # 둘다 다음 인덱스로
            t_i += 1
        else:                               # 트럭의 적재용량 < 화물의 무게라면
            w_i += 1                        # 다음 가벼운 화물로

    print(f'#{tc} {ans}')
