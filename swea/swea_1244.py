# swea 1244 최대 상금
def f(i, n, c):
    global maxV
    global minC
    if c == 0 or i == n:    # 교환횟수가 0이거나 기준위치가 맨 오른쪽 카드까지 고려된 경우
        # 현재 숫자판 순서로 최대값과 비교
        # 기존의 최대값과 같으면 교환횟수가 큰 쪽을 선택
        s = 0
        for x in card:
            s = s*10 + x

        if maxV < s:
            maxV = s
            minC = c
        elif maxV == s and minC > c:    # 더 많은 교환횟수를 소모
            minC = c

    else:
        for j in range(n):
            if i != j:      # 자기 자신을 제외하고 교환횟수 1에 해당하는 위치와 교환
                card[i], card[j] = card[j], card[i]
                f(i+1, n, c-1)
                card[i], card[j] = card[j], card[i]
            else:  # 기준위치만 바꾸고 교환없는 호출
                f(i+1, n, c)


T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    card = list(map(int, num))
    maxV = 0                    # 최대상금
    minC = int(cnt)             # 최대상금을 만들고 남은 교환횟수
    f(0, len(card), int(cnt))   # 교환 기준 위치, 숫자판 개수, 교환횟수

    #print(tc, maxV, minC)
    if minC % 2:    # 교환 횟수가 홀수번 남은 경우
        n1 = maxV % 10
        n2 = maxV % 100 // 10
        maxV = maxV // 100 * 100 + n1 * 10 + n2

    print(f'#{tc} {maxV}')
