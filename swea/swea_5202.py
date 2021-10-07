# swea 5202 화물 도크
# Programming/Advanced/탐욕 알고리즘

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = [tuple(map(int, input().split()))
                for _ in range(N)]     # 작업 신청서

    end = 24        # 검사 시간
    cnt = 0         # 최대 화물차의 개수
    while True:
        max_s = -1          # 검사 시간에 대해 가장 늦은 시작시간
        for i in range(N):  # 모든 신청엗 대해
            # 끝나는 시간 < 검사 시간 AND 시작시간 > 가장 늦은 시작시간인 경우
            if schedule[i][1] <= end and schedule[i][0] >= max_s:
                # 가장 늦은 시작 시간 갱신
                max_s = schedule[i][0]
        end = max_s                                                 # 검사 시간 갱신

        if max_s == -1:                                             # 검사 시간 이하로 신청차량이 없으면 종료
            break
        else:                                                       # 신청 차량이 있으면 화물차 개수 하나 증가
            cnt += 1

    print(f'#{tc} {cnt}')
