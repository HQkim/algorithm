# swea 2005 파스칼의 삼각형

def pascal(n):
    arr = [[0]*n for _ in range(n)]  # n x n 배열 만들기

    for i in range(n):
        for j in range(i+1):        # 대각선 까지만 계산하기
            if j == 0 or i == j:    # 첫열이거나 대각선인 경우 1
                arr[i][j] = 1
            else:                   # 이외는 전행을 통해 계산
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = pascal(N)

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i][:i+1])
