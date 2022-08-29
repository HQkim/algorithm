# BOJ 3190 뱀
from collections import deque
import sys


def snake_progress():
    t, d = 0, 0     # 현재 시간, 방향
    r, c = 1, 1     # 현재 위치 : 행,열
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(1, 1)])
    for i in range(L+1):
        if i != L:                          
            X, C = input().rstrip().split() 
            X = int(X)
        else:                                       # 마지막 방향전환 이후에 이동하는 경우
            X = t + N

        for time in range(t+1, X+1):
            nr = r + directions[d][0]
            nc = c + directions[d][1]
            if 0 < nr <= N and 0 < nc <= N:
                if (nr, nc) in q:                   # 자신의 몸통과 만나면 종료
                    return time 
                else:
                    if graph[nr][nc]:               # 사과가 있는 경우 : 사과가 없어지고 꼬리는 움직이지 않음
                        graph[nr][nc] = 0
                        q.appendleft((nr, nc))
                    else:                           # 사과가 없는 경우 : 꼬리가 위치한 칸 비워주기
                        q.appendleft((nr, nc))
                        q.pop()
                r, c = nr, nc
            else:                                   # 벽과 만나면 종료
                return time
        
        t = X           # 시간 갱신  
                                
        if C == 'L':    # 방향 전환
            d -= 1
        else:
            d += 1
        d %= 4
    

input = sys.stdin.readline

N = int(input())
K = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

L = int(input())

print(snake_progress())

        


