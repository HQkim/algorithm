# swea 5174 subtree
# Programming Intermediate > Tree

def pre_order(n):                      # 전위 순회
    global count                       # 글로벌 변수로 노드 카운팅
    if n:
        count += 1
        pre_order(left[n])
        pre_order(right[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    left = [0] * (E + 2)                # 왼쪽 자식
    right = [0] * (E + 2)               # 오른쪽 자식

    edges = list(map(int, input().split()))
    for i in range(E):                              # 간선 정보 입력
        parent, child = edges[i*2], edges[i*2+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    count = 0

    pre_order(N)

    print(f'#{tc} {count}')
