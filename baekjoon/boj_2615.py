# BOJ 2615 오목

def check():
    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                color = board[x][y]

                for i in range(4):
                    cnt = 1
                    nx = x + dx[i]
                    ny = y + dy[i]

                    while 0<=nx<19 and 0<=ny<19 and board[nx][ny] == color:
                        cnt += 1

                        if cnt == 5:
                            if 0<=x-dx[i]<19 and 0<=y-dy[i]<19 and board[x-dx[i]][y-dy[i]] == color:
                                break
                            if 0<=nx+dx[i]<19 and 0<=ny+dy[i]<19 and board[nx+dx[i]][ny+dy[i]] == color:
                                break
                            print(color)
                            print(x + 1, y + 1)
                            return

                        nx += dx[i]
                        ny += dy[i]
    
    print(0)

board = [list(map(int, input().split())) for _ in range(19)]
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
check()

# 시도 자체가 매우 많았다.
# 인덱스 계산에 대해서 조금 더 익숙해진것 같다.