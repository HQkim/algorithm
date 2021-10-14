# swea 5247 연산
# programming advanced/그래프의 기본과 탐색
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque()                     # 자연수를 담을 큐 생성
    queue.append((N, 0))                # 현재 자연수와 연산 횟수를 큐에 담기
    check = {}                          # 계산된 적 있는 자연수인지 체크할 딕셔너리
    check[N] = 1

    while queue:
        num, cnt = queue.popleft()
        check[num] = 1                  # 계산된 적 없었다면 이제 계산될 것이므로 딕셔너리에 기록
        if num == M:                    # M값과 같아지면 반복문 탈출
            break

        for v in [num+1, num-1, num*2, num-10]:
            if not check.get(v, 0) and 0 < v <= 1000000:
                queue.append((v, cnt+1))
                check[v] = 1

    print(f'#{tc} {cnt}')
