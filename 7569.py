# 7569번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m, n, h = map(int, input().rstrip().split())

graph = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]


def solution(h, n, m, graph):
    
    # 토마토가 이미 모두 익었는지 체크
    already_check = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    already_check += 1
    
    if already_check == 0:
        return 0

    graph_test = graph.copy()
    # 토마토 모두 익힐 수 있는지 체크
    def dfs(z, x, y):
        global m, n, h
        if x < 0 or x > n-1 or y < 0 or y > m-1 or z < 0 or z > h-1:
            return

        if graph_test[z][x][y] == 1:
            
            dfs(z, x-1, y)
            dfs(z, x+1, y)
            dfs(z, x, y-1)
            dfs(z, x, y+1)
            dfs(z-1, x, y)
            dfs(z+1, x, y)
            return
        return

    for i in range(h):
        for j in range(n):
            for k in range(m):
                dfs(i, j, k)

    not_check = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph_test[i][j][k] == 0:
                    not_check += 1

    print(graph_test)

    if not_check != 0:
        return -1
    else:
        return 1


print(solution(h, n, m, graph))