# swea 1486 장훈이의 높은 선반

def f(i, h, res):
    global N, B, min_diff

    if h >= B:                          # 순회 도중에 B보다 크거나 같다면 종료
        diff = h - B
        min_diff = min(min_diff, diff)
        return

    if i == N-1 and h+H[i] >= B:        # 마지막 인덱스까지 왔고 현재 높이에 H[i]를 더한 것이 B보다 크거나 같다면
        h += H[i]
        diff = h - B
        min_diff = min(min_diff, diff)
        return

    if h + res < B:         # 남은 높이와 현재 높이를 더한 것이 B보다 낮으면 가망이 없으므로 종료
        return

    f(i+1, h+H[i], res-H[i])    # H[i]를 높이에 더하는 경우
    f(i+1, h, res-H[i])         # H[i]를 높이에 더하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_diff = int(10e9)

    f(0, 0, sum(H))     # 몇번째 자리의 점원의 키를 체크하는지, 현재 높이, 남은 높이

    print(f'#{tc} {min_diff}')
