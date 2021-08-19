# swea 1961 숫자 배열 회전
def rotate_array(arr):                          # 시계 방향으로 90도 회전시켜서 반환하는 함수
    arr_rotated = list(map(list, zip(*arr)))    # transpose를 시킨 후에
    for i in range(len(arr)):                   # 각 행을 뒤집기
        arr_rotated[i].reverse()
    return arr_rotated


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr_90 = rotate_array(arr)
    arr_180 = rotate_array(arr_90)
    arr_270 = rotate_array(arr_180)

    print(f'#{tc}')
    for i in range(N):
        print("".join(arr_90[i]), end=" ")
        print("".join(arr_180[i]), end=" ")
        print("".join(arr_270[i]), end=" ")
        print()
