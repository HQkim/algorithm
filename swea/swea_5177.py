# swea 5177 이진 힙
# Programming Intermediate > Tree

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)                                  # 완전 이진 트리
    numbers = [0] + list(map(int, input().split()))      # 입력할 숫자들

    for i in range(1, N+1):
        tree[i] = numbers[i]                            # 트리에 순차적으로 숫자 추가

        # 최소힙 구현
        child = i
        while True:
            parent = child // 2
            if parent == 0:                         # 루트 노드인 경우 종료
                break

            if tree[parent] > tree[child]:          # 부모가 자식보다 크다면 스왑
                tree[parent], tree[child] = tree[child], tree[parent]
                child = parent
            else:                                   # 부모가 자식보다 작다면 종료
                break

    # 조상 노드에 저장된 정수의 합 계산
    total = 0
    child = N
    while True:
        parent = child // 2
        if parent == 0:
            break

        total += tree[parent]
        child = parent

    print(f'#{tc} {total}')
