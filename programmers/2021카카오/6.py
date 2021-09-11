def change_board(board, s):
    status, r1, c1, r2, c2, degree = s
    if status == 1:
        degree = -degree
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            board[i][j] += degree

    return board


def solution(board, skill):
    for s in skill:
        board = change_board(board, s)

    answer = 0
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1
    return answer


solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
         [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])
