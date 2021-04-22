# 7576번

import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

def solution(n, m, graph):
    queue = deque([])
    queue_temp = deque([])

    # 토마토가 이미 모두 익었는지 체크
    already_check = 0
    for j in range(n):
        for k in range(m):
            if graph[j][k] == 0:
                already_check += 1
            if graph[j][k] == 1:
                queue.append((j,k,0))
    
    if already_check == 0:
        return 0

    graph_ripe = graph.copy()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # 주변 익히기
    def ripe(j, k, d):
        for i in range(4):
            n_x = j + dx[i]
            n_y = k + dy[i]

            if n_x<0 or n_x>=n or n_y<0 or n_y>=m or graph_ripe[n_x][n_y]==-1:
                continue
            if graph_ripe[n_x][n_y]==0:
                graph_ripe[n_x][n_y]=1
                queue_temp.append((n_x,n_y,d+1))


    # bfs로 익히는 과정 진행
    while queue:
        
        for j,k,d in queue:
            ripe(j,k,d)
        for _ in range(len(queue)):
            x,y,d = queue.popleft()
        if queue_temp:
            for _ in range(len(queue_temp)):
                queue.append(queue_temp.popleft())
        

    ripe_check = 0
    for j in range(n):
        for k in range(m):
            if graph_ripe[j][k] == 0:
                ripe_check += 1
    if ripe_check == 0:
        return 
    else:
        return -1

print(solution(n, m, graph))