import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().rstrip().split())

graph = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]
day = 0

def solution1(h, n, m, graph):
    queue = deque([])
    queue_temp = deque([])

    # 토마토가 이미 모두 익었는지 체크
    already_check = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    already_check += 1
                if graph[i][j][k] == 1:
                    queue.append((i,j,k))
    
    if already_check == 0:
        return 0

    graph_ripe = graph.copy()

    # 주변 익히기
    def ripe(i, j, k):
        i_list = []
        j_list = []
        k_list = []
        if i-1 >= 0:
            i_list.append(i-1)
        if i+1 <= h-1:
            i_list.append(i+1)
        if j-1 >= 0:
            j_list.append(j-1)
        if j+1 <= n-1:
            j_list.append(j+1)
        if k-1 >= 0:
            k_list.append(k-1)
        if k+1 <= m-1:
            k_list.append(k+1)

        for z in i_list:
            if graph_ripe[z][j][k] == 0:
                graph_ripe[z][j][k] = 1
                queue_temp.append((z,j,k))
        for x in j_list:
            if graph_ripe[i][x][k] == 0:
                graph_ripe[i][x][k] = 1
                queue_temp.append((i,x,k))
        for y in k_list:
            if graph_ripe[i][j][y] == 0:
                graph_ripe[i][j][y] = 1
                queue_temp.append((i,j,y))

    # bfs로 익히는 과정 진행
    while queue:
        global day
        day += 1
        for i,j,k in queue:
            ripe(i,j,k)
        for _ in range(len(queue)):
            queue.popleft()
        if queue_temp:
            for _ in range(len(queue_temp)):
                queue.append(queue_temp.popleft())
        
        already_ripe_check = 0
        b = 0
        for i in range(h):
            if b != 0:
                break
            for j in range(n):
                if b != 0:
                    break
                for k in range(m):
                    if graph_ripe[i][j][k] == 0:
                        already_ripe_check = 1
                        b = 1
                        break
        if already_ripe_check == 0:
            break

    ripe_check = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph_ripe[i][j][k] == 0:
                    ripe_check += 1
    if ripe_check == 0:
        return day
    else:
        return -1

def solution2(h, n, m, graph):
    queue = deque([])
    queue_temp = deque([])

    # 토마토가 이미 모두 익었는지 체크
    already_check = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    already_check += 1
                if graph[i][j][k] == 1:
                    queue.append((i,j,k,0))
    
    if already_check == 0:
        return 0

    graph_ripe = graph.copy()

    # 주변 익히기
    def ripe(i, j, k, d):
        di=[1,-1,0,0,0,0]
        dj=[0,0,1,-1,0,0]
        dk=[0,0,0,0,1,-1]

        for p in range(6):
            n_i = i + di[p]
            n_j = j + dj[p]
            n_k = k + dk[p]

            if n_i<0 or n_j<0 or n_k<0 or n_i>=h or n_j>=n or n_k>=m or graph_ripe[n_i][n_j][n_k]==-1:
                continue
            if graph[n_i][n_j][n_k] == 0:
                graph[n_i][n_j][n_k] = 1
                queue_temp.append((n_i,n_j,n_k,d+1))

    # bfs로 익히는 과정 진행
    while queue:
        for i,j,k,d in queue:
            ripe(i,j,k,d)
        for _ in range(len(queue)):
            z,x,y,d = queue.popleft()
        if queue_temp:
            for _ in range(len(queue_temp)):
                queue.append(queue_temp.popleft())

    ripe_check = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph_ripe[i][j][k] == 0:
                    ripe_check += 1
    if ripe_check == 0:
        return d
    else:
        return -1


print(solution1(h, n, m, graph))

# solution1이 solution2보다 2배 빠르다고 나온다. 하지만 solution1을 2차원 토마토 문제에 넣으니 40프로에서시간초과... 3차원이 더 빠르게 익어서 그런가?..