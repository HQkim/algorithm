# swea 7465 창용 마을 무리의 개수

def find_rep(x):                    # 현재 집단의 대표를 찾는 함수
    if x == rep[x]:
        return x
    return find_rep(rep[x])


def union(a, b):                    # 두 사람이 속한 집단을 합치는 함수
    rep[find_rep(b)] = find_rep(a)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    rep = [i for i in range(N+1)]           # 각 사람이 속한 대표를 나타내는 배열

    for _ in range(M):
        a, b = map(int, input().split())
        if find_rep(a) < find_rep(b):       # 대표 번호가 작은 쪽으로 집단 합치기
            union(a, b)
        else:
            union(b, a)

    cnt = 0
    for i in range(1, N+1):                 # 자기 자신이 대표인 경우만 집단의 개수
        if rep[i] == i:
            cnt += 1

    print(f'#{tc} {cnt}')
