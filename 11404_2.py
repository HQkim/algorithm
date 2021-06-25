import sys

input = sys.stdin.readline
INF = int(10e9)


def solution():

    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        if c < graph[a][b]:
            graph[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                temp = graph[i][k] + graph[k][j]
                if temp < graph[i][j]:
                    graph[i][j] = temp

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost = graph[i][j]
            if cost == INF:
                print(0, end=" ")
            else:
                print(cost, end=" ")
        print()

    return


solution()
