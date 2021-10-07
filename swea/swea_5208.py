# swea 5208 전기버스
# Programming/Advanced/백트래킹

def f(i, c, N):                 # 현재 위치, 충전한 횟수, 충전소 개수
    global min_c
    if i == N-1:                # 도착점에 도달하면 최소충전횟수 갱신
        c -= 1
        min_c = min(c, min_c)
        return

    if c >= min_c:              # 현재 충전한 횟수가 최소 충전횟수보다 크거나 같아지면 가지치기
        return

    min_m = min(i+M[i]+1, N)
    for j in range(i+1, min_m):  # 갈 수 있는 정류장에 대해 순회
        f(j, c+1, N)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]              # 충전소 개수
    M = arr[1:]             # 충전소별 이동거리 배열

    min_c = N               # 최소충전횟수
    f(0, 0, N)

    print(f'#{tc} {min_c}')
