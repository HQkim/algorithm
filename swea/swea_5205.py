# swea 5205 퀵 정렬
# Programming/Advanced/분할 정복

def quick_sort(left, right):            # left는 정렬할 배열의 시작 인덱스, right는 끝 인덱스
    if left < right:
        s = hoare(left, right)          # 왼쪽은 s인덱스 값보다 낮고 오른쪽은 s인덱스보다 높게 구분
        quick_sort(left, s-1)           # 왼쪽에 대해 quick sort
        quick_sort(s+1, right)          # 오른쪽에 대해 quick sort


def hoare(left, right):                 # 피봇 값을 기준으로 좌우로 나누는 함수
    i, j = left, right
    p = A[left]                         # 피봇 값을 정렬할 배열의 시작 값으로
    while i <= j:                       # i, j 가 교차하지 않을 때까지
        while i <= j and A[i] <= p:     # i, j가 교차하지 않고 A[i]값이 피봇 값보다 작을때까지 i 증가
            i += 1
        while i <= j and A[j] >= p:     # i, j가 교차하지 않고 A[j]값이 피봇 값보다 클때까지 j 감소
            j -= 1
        # i, j 가 교차하지 않았다면 A[i]는 피봇보다 크고 A[j]는 피봇보다 작으므로 스왑
        if i < j:
            A[i], A[j] = A[j], A[i]
    # A[j]는 피봇보다 작은 값들 중에 가장 오른쪽에 있으므로 피봇과 위치 교환
    A[left], A[j] = A[j], A[left]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(0, len(A)-1)

    print(f'#{tc} {A[N//2]}')
