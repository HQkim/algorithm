def inorder_traverse(v, N):         # 중위 순회 (완전 이진 트리)
    if v <= N:
        inorder_traverse(v*2, N)
        print(f'{tree[v]}', end="")
        inorder_traverse(v*2+1, N)


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(1, N+1):     
        info = input().split()
        tree[i] = info[1]           # 문자만 저장

    print(f'#{tc}', end=" ")
    inorder_traverse(1, N)
    print()