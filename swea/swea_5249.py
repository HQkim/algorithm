# swea 5249 최소 신장 트리
# programming advanced/그래프의 최소 비용문제

def find_set(x):            # 노드가 속한 집합의 대표를 찾는 함수
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):                    # 두 노드가 속한 집합을 합치기
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())            # 마지막 노드 번호, 간선의 개수
    edge = []                                   # 간선 정보를 담을 인접 리스트
    for _ in range(E):                          # 인접 리스트에 정보 담기
        u, v, w = map(int, input().split())
        edge.append([w, u, v])
    edge.sort()                                 # 가중치 순으로 오름차순 정렬
    rep = [i for i in range(V+1)]               # 각 노드별 대표 정보를 담을 리스트
    cnt = 0
    ans = 0
    for w, u, v in edge:
        if find_set(v) != find_set(u):
            cnt += 1
            union(u, v)
            ans += w
            if cnt == V:                        # 노드의 개수는 V+1개이니 V만큼의 간선이 선택되면 종료
                break
    print(f'#{tc} {ans}')
