# swea 5178 노드의 합
# Programming Intermediate > Tree

def postorder_traverse(v, N):           # 후위 순회
    if v <= N:                          # 완전 이진 트리 범위 안에 있는 경우
        postorder_traverse(v*2, N)
        postorder_traverse(v*2+1, N)
        if v*2 <= N:                    # 왼쪽 자식이 있는 경우
            a = tree[v*2]
        else:
            a = 0
        if v*2+1 <= N:                  # 오른쪽 자식이 있는 경우
            b = tree[v*2+1]
        else:
            b = 0

        if a == b == 0:                 # 자식이 없는 경우
            pass
        else:
            tree[v] = a + b


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):                          # 리프 노드값 트리에 할당
        node, value = map(int, input().split())
        tree[node] = value

    postorder_traverse(1, N)

    print(f'#{tc} {tree[L]}')
