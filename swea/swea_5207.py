# swea 5207 이진 탐색
# Programming/Advanced/분할 정복
def binary_search(left, right, t):      # 이진탐색을 통하여 조건에 맞는지 확인하는 함수
    s = left
    e = right

    direction = -1
    is_exist = False                    # 찾는 수가 references에 있는지 나타내는 플래그
    is_cross = True                     # 이진탐색을 하면서 번갈아 교차하는지 나타내는 플래그
    while s <= e:
        mid = (s + e) // 2
        if t == references[mid]:
            is_exist = True
            break
        elif t < references[mid]:
            e = mid - 1
            if direction == 0:
                is_cross = False
            direction = 0
        else:
            s = mid + 1
            if direction == 1:
                is_cross = False
            direction = 1

    if is_exist and is_cross:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    references = list(map(int, input().split()))    # 주어진 배열 reference
    references.sort()
    # reference에 있는지 확인할 수들을 담은 배열
    targets = list(map(int, input().split()))

    cnt = 0
    for t in targets:
        cnt += binary_search(0, N-1, t)             # 시작 인덱스, 끝 인덱스, 찾을 수 t

    print(f'#{tc} {cnt}')
