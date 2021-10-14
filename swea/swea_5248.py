# swea 5248 그룹 나누기
# programming advanced/그래프의 기본과 탐색

def find_set(x):                    # 그룹의 대표를 찾는 함수
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):                    # 그룹을 합치는 함수
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    applications = list(map(int, input().split()))  # 같은 조에 참여하고 싶은 사람을 적은 신청서
    rep = [i for i in range(N+1)]                   # 같은 조의 대표

    for i in range(M):                              # 모든 신청에 대해 그룹 합치기
        a, b = applications[i*2:i*2+2]
        union(a, b)

    ans_set = set()                         # 대표를 저장하는 세트
    for i in range(1, N+1):
        ans_set.add(find_set(i))            # 모든 번호들에 대해 대표들을 제출하기

    print(f'#{tc} {len(ans_set)}')
