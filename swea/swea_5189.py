# swea 5189 전자카트
# Programming/Advanced/완전 검색

def f(i, cnt, n, s):
    global minV
    if cnt == n-1:      # 모두 방문했을 때
        s += e[i][0]    # 사무실로 돌아가는 사용량 더해주기
        if s < minV:    # 최소 배터리 사용량보다 배터리 사용량이 작다면 갱신
            minV = s
        return

    if s >= minV:       # 최소 배터리 사용량보다 커진다면 중지
        return

    for x in range(n):
        if not visited[x]:  # 방문하지 않은 구역을 방문
            visited[x] = 1
            f(x, cnt+1, n, s+e[i][x])
            visited[x] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 구역의 개수
    e = [list(map(int, input().split())) for _ in range(N)]  # 배터리 사용량 표

    minV = 100 * N      # 최소 배터리 사용량
    # 구역별 방문 여부 체크 (각 구역은 편의상 -1을 해서 계산한다. ex)1번 구역은 인덱스에서 0번)
    visited = [0] * N
    visited[0] = 1      # 사무실은 방문한 것으로 체크

    f(0, 0, N, 0)   # 현재 위치, 이동횟수, 구역의 개수, 배터리 사용량

    print(f'#{tc} {minV}')
