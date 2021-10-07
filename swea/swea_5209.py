# swea 5209 최소 생산 비용
# Programming/Advanced/백트래킹

def f(c, v, N):
    global min_value
    if c == N:                          # 제품을 다 공장에 할당했으면 종료
        min_value = min(v, min_value)
        return

    if v >= min_value:                  # 중간에 현재비용이 최소비용을 넘어갈 때 종료
        return

    for i in range(N):
        if not visited_factory[i]:      # 방문하지 않은 공장에 대하여 c번째 제품 할당
            visited_factory[i] = 1
            f(c+1, v+graph[c][i], N)
            visited_factory[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited_factory = [0] * N       # 방문한 공장 표시
    min_value = 99 * N              # 최소 비용

    f(0, 0, N)                      # 몇번째 제품(0~N-1까지), 현재비용, 제품(공장)의 수

    print(f'#{tc} {min_value}')
