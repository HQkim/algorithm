# swea 2806 N-Queen

def f(i, N):
    global ans
    if i == N:
        ans += 1
        return

    for x in range(N):
        if visited[i] == -1:
            visited[i] = x
            is_valid = True
            for j in range(i):
                # 같은 열에 있거나 대각선에 있는 경우 제외
                if x == visited[j] or abs(visited[j]-x) == abs(i-j):
                    is_valid = False
                    break
            if is_valid:
                f(i+1, N)
            visited[i] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [-1]*N        # 각 행별 퀸의 위치를 나타내는 배열, -1이면 아직 배치되지 않은 경우
    ans = 0
    f(0, N)

    print(f'#{tc} {ans}')
