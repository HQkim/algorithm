# programmers 게임 맵 최단거리

from collections import deque

# 시작 위치는 (0,0)
# 벽이 0, 길은 1            
def solution(maps):

    def bfs(maps, x, y):
        # x, y는 시작지점 여기서는 0, 0
        row = len(maps)
        col = len(maps[0])
        queue = deque()
        queue.append((x,y))
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while queue:
            x, y = queue.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if -1 < nx < row and -1 < ny < col and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        if maps[row-1][col-1] == 1:
            maps[row-1][col-1] = -1
        return maps[row-1][col-1]

    return bfs(maps, 0, 0)