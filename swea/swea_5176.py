# swea 5176 이진탐색
# Programming Intermediate > Tree

def inorder(v, N):          # 중위 순회
    global num                  # 1부터 시작해서 점차 증가
    if v <= N:                  # 완전 이진 트리 범위 안이라면
        inorder(v*2, N)         # 가장 왼쪽 아래부터 숫자 채우기
        tree[v] = num
        num += 1
        inorder(v*2+1, N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)          # 완전 이진 트리 -> 1차원 배열로 구현
    num = 1

    inorder(1, N)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
