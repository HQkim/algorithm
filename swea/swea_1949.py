# swea 1949 등산로 조성

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
