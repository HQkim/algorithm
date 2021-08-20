# swea 1961 숫자 배열 회전

# 배열 자체를 돌린 풀이 (zip 활용)
# def rotate_array(arr):                          # 시계 방향으로 90도 회전시켜서 반환하는 함수
#     arr_rotated = list(map(list, zip(*arr)))    # transpose를 시킨 후에
#     for i in range(len(arr)):                   # 각 행을 뒤집기
#         arr_rotated[i].reverse()
#     return arr_rotated


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]

#     arr_90 = rotate_array(arr)
#     arr_180 = rotate_array(arr_90)
#     arr_270 = rotate_array(arr_180)

#     print(f'#{tc}')
#     for i in range(N):
#         print("".join(arr_90[i]), end=" ")
#         print("".join(arr_180[i]), end=" ")
#         print("".join(arr_270[i]), end=" ")
#         print()

# 다른 풀이(인덱스만 이용)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr_90 = [[0]*N for _ in range(N)]
    arr_180 = [[0]*N for _ in range(N)]
    arr_270 = [[0]*N for _ in range(N)]

    for i in range(N):                          # 90도 회전한 배열 구하기
        for j in range(N):
            arr_90[j][N-i-1] = arr[i][j]
    for i in range(N):                          # 180도 회전한 배열 구하기
        for j in range(N):
            arr_180[j][N-i-1] = arr_90[i][j]
    for i in range(N):                          # 270도 회전한 배열 구하기
        for j in range(N):
            arr_270[j][N-i-1] = arr_180[i][j]

    print('#{}'.format(tc))
    for i in range(N):
        print("".join(arr_90[i]), "".join(arr_180[i]), "".join(arr_270[i]))
