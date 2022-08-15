# BOJ 1025 제곱수 찾기

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

max_square = -1
for i in range(N):      # 행 시작 위치
    for j in range(M):  # 열 시작 위치
        for k in range(-N, N):        # 행의 공차, -N부터로 잡는 것은 N,M이 모두 1일 때 코드가 돌아가도록 하기 위함
            for m in range(-M, M):    # 열의 공차
                if k == 0 and m == 0: continue  # 무한 루프 제거
                x = i
                y = j
                num = ''
                while 0 <= x < N and 0 <= y < M:
                    num += arr[x][y]
                    if (int(num)**0.5)%1 == 0:   # 제곱수 판별
                        max_square = max(max_square, int(num))
                    x += k
                    y += m

print(max_square)