# swea 1865 동철이의 일 분배

def f(j, s, N):
    global max_s
    if j == N:                  # 일이 다 할당되었으면 최대 확률과 비교후 갱신
        max_s = max(s, max_s)
        return

    if s <= max_s:              # 현재확률이 최대확률보다 낮거나 같으면 중단
        return

    for i in range(N):
        if not visited[i]:      # 일이 할당 안된 직원에게 일 할당후 재귀로 순회
            visited[i] = 1
            f(j+1, s*P[i][j]*0.01, N)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_s = 0

    f(0, 1, N)      # 처리할 일의 번호, 현재확률, 일의 총개수

    print(f'#{tc} {max_s*100:.6f}')
