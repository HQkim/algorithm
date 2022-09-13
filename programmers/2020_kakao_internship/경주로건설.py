# programmers 2020카카오인턴십 경주로건설

def solution(board):
    INF = int(10e9)
    N = len(board[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    dp = [[INF]*N for _ in range(N)]

    def dfs(r, c, d, cost):
        if cost > dp[r][c]:
            return
        
        dp[r][c] = cost

        if r == N-1 and c == N-1:
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
                board[nr][nc] = 1
                if r == 0 and c == 0:
                    dfs(nr, nc, i, cost+100)
                else:
                    if (i + d) % 2 == 0:
                        dfs(nr, nc, i, cost+100)
                    else:
                        dfs(nr, nc, i, cost+600)
                board[nr][nc] = 0

    board[0][0] = 1
    dfs(0, 0, 0, 0)

    return dp[-1][-1]
