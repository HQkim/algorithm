# swea 6485 삼성시의 버스 노선

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    edges = []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        edges.append((Ai, Bi))

    P = int(input())
    nodes = []
    for _ in range(P):
        Cj = int(input())
        nodes.append(Cj)

    count = [0] * P
    for i in range(P):
        Cj = nodes[i]
        for edge in edges:
            Ai, Bi = edge
            if Ai <= Cj <= Bi:
                count[i] += 1

    print(f'#{tc}', end=" ")
    for i in range(P):
        print(f'{count[i]}', end=" ")
    print()

# 그냥 길이 5001짜리 array 만들어서 해도 된다.
