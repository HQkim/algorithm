# swea 4466 최대 성적표 만들기

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr_k = arr[N-K:]
    print(f'#{tc} {sum(arr_k)}')
