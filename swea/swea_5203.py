# swea 5203 베이비진 게임
# Programming/Advanced/탐욕 알고리즘

def is_baby_gin(arr):       # 베이비진인지 확인하는 함수
    # run 찾기
    arr_set = set(arr)
    arr_u = list(arr_set)
    arr_u.sort()
    if len(arr_u) >= 3:
        cnt = 1
        for x in range(1, len(arr_u)):
            if arr_u[x] == arr_u[x-1] + 1:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return True

    # triplet 찾기
    arr_count = []
    for x in arr_set:
        arr_count.append(arr.count(x))

    if max(arr_count) >= 3:
        return True

    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))     # 입력할 카드

    p1 = []                                     # 플레이어1이 받은 카드
    p2 = []                                     # 플레이어2가 받은 카드

    is_p1_baby_gin = False                      # p1의 카드가 베이비진인지 나타내는 변수
    is_p2_baby_gin = False                      # p2의 카드가 베이비진인지 나타내는 변수
    i = 0
    while i <= 11:
        if i % 2 == 0:
            p1.append(cards[i])
        else:
            p2.append(cards[i])

        if len(p1) >= 3:
            is_p1_baby_gin = is_baby_gin(p1)

        if len(p2) >= 3:
            is_p2_baby_gin = is_baby_gin(p2)

        if is_p1_baby_gin or is_p2_baby_gin:
            break

        i += 1

    if is_p1_baby_gin and not is_p2_baby_gin:
        ans = 1
    elif not is_p1_baby_gin and is_p2_baby_gin:
        ans = 2
    else:
        ans = 0

    print(f'#{tc} {ans}')
