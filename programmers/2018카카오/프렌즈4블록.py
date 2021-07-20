from collections import deque


def solution(m, n, board):

    graph = [[i for i in line] for line in board]
    answer = 0

    while True:
        count, graph = delete_box_in_graph(m, n, graph)
        if count == 0:
            break
        answer += count
        graph = makeup_graph(m, n, graph)

    return answer


def delete_box_in_graph(m, n, board):
    check = [[0]*n for _ in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != 0:
                character = board[i][j]
                if board[i][j+1] == character and board[i+1][j] == character and board[i+1][j+1] == character:
                    check[i][j] = check[i+1][j] = check[i][j +
                                                           1] = check[i+1][j+1] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if check[i][j]:
                board[i][j] = 0
                count += 1

    return (count, board)


def makeup_graph(m, n, graph):
    column_list = []
    for i in range(n):
        column_list.append([line[i] for line in graph])
    stack_list = [[i for i in line if i != 0] for line in column_list]

    for i in range(n):
        length_of_stack = len(stack_list[i])
        stack_list[i] = deque(stack_list[i])
        for _ in range(m-length_of_stack):
            stack_list[i].appendleft(0)

    for i in range(n):
        stack_list[i] = list(stack_list[i])

    new_graph = []
    for i in range(m):
        new_graph.append([line[i] for line in stack_list])

    return new_graph


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
