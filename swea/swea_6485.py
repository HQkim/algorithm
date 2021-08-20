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

# 방법 2
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())        # 버스 노선 수
 
#     start = [0] * 5001      # 출발 정류장 표시
#     end = [0] * 5001        # 도착 정류장 표시
#     bus_stop = [0] * 5001   # 계산한 버스 표시

#     for i in range(N):
#         A, B = map(int, input().split())
#         start[A] += 1
#         end[B] += 1

#     # 버스 계산
#     for i in range(len(bus_stop) - 1):
#         bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]

#     P = int(input())
#     print("#{}".format(tc), end=" ")
#     for i in range(P):
#         C = int(input())
#         print(bus_stop[C], end=" ")
#     print()

# 방법 3
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())

#     bus_stop = [0] * 5001

#     for i in range(N):
#         A, B = map(int, input().split())

#         for j in range(A, B+1):
#             bus_stop[i] += 1

#     P = int(input())
#     print("#{}".format(tc), end=" ")
#     for i in range(P):
#         C = int(input())
#         print(bus_stop[C], end=" ")
#     print()    
