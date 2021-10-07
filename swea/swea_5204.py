# swea 5204 병합 정렬
# Programming/Advanced/분할 정복

def merge_sort(arr):                # 병합 정렬 함수
    if len(arr) == 1:               # 배열의 길이가 1이면 그 자체 리턴
        return arr

    mid = len(arr) // 2             # 가운데 인덱스
    left = merge_sort(arr[:mid])    # 왼쪽 배열
    right = merge_sort(arr[mid:])   # 오른쪽 배열

    return merge(left, right)       # 왼쪽과 오른쪽을 병합한 배열 리턴


def merge(left, right):             # 왼쪽 배열과 오른쪽 배열 병합하는 함수
    global cnt
    result = []
    left_ind = 0
    right_ind = 0
    left_len = len(left)
    right_len = len(right)
    if left_len and right_len:      # 왼쪽 배열의 마지막 값이 오른쪽 배열의 마지막 값보다 큰 경우 카운팅
        if left[-1] > right[-1]:
            cnt += 1

    while left_ind < left_len or right_ind < right_len:     # 두 배열의 원소가 남을 때까지
        if left_ind < left_len and right_ind < right_len:   # 두 배열에 모두 원소가 있는 경우
            if left[left_ind] <= right[right_ind]:          # 작은 쪽을 결과 배열에 담기
                result.append(left[left_ind])
                left_ind += 1
            else:
                result.append(right[right_ind])
                right_ind += 1
        elif left_ind < left_len:                           # 왼쪽 배열에만 원소가 남은 경우
            result.append(left[left_ind])
            left_ind += 1
        else:                                               # 오른쪽 배열에만 원소가 남은 경우
            result.append(right[right_ind])
            right_ind += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0

    b = merge_sort(a)
    mid = N // 2

    print(f'#{tc} {b[mid]} {cnt}')

# merg_sort()함수에서 매번 배열을 새롭게 만드는 것보다 시작 인덱스와, 끝 인덱스를 함수 인자로 주는 방법이 있다.
# 정지웅님 코드
# def mergeSort(low, high):
#     global ans
#     if low == high:
#         return
#     mid = (low + high + 1) // 2
#     mergeSort(low, mid - 1)
#     mergeSort(mid, high)
#     if ai[mid - 1] > ai[high]:
#         ans += 1
#     i, j, k = low, mid, low
#     while i <= mid - 1 and j <= high:
#         if ai[i] <= ai[j]:
#             arr[k] = ai[i]
#             k, i = k + 1, i + 1
#         else:
#             arr[k] = ai[j]
#             k, j = k + 1, j + 1
#     while i <= mid - 1:
#         arr[k] = ai[i]
#         k, i = k + 1, i + 1
#     while j <= mid:
#         arr[k] = ai[j]
#         k, j = k + 1, j + 1
#     for x in range(low, high + 1):
#         ai[x] = arr[x]


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     ai = list(map(int, input().split()))
#     arr = [0] * N
#     ans = 0
#     mergeSort(0, N - 1)
#     print('#{} {} {}'.format(tc, ai[N // 2], ans))
