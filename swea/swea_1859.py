# swea 1859 백만 장자 프로젝트
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arry = list(map(int, input().split()))

    profit = 0                              # 이익
    max_value = arry[-1]                    # 현재 최대값

    for i in range(N-1, -1, -1):            # 뒤에서부터 탐색
        if max_value > arry[i]:             # 현재 최대값보다 탐색하는 값이 작으면 사고 팔기
            profit += max_value - arry[i]
        else:                               # 현재 최대값보다 탐색하는 값이 크면 현재 최대값 갱신
            max_value = arry[i]

    print(f'#{tc} {profit}')

# https://unnamed-it.tistory.com/26 참고
