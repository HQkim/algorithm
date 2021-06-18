# 백준 2206번 벽 부수고 이동하기

import sys
from collections import deque


def main():
    row, column, graph = input_graph()
    answer = break_wall_and_move(row, column, graph)
    print(answer)
    return


def input_graph():
    input = sys.stdin.readline
    row, column = map(int, input().rstrip().split())
    graph = [[int(i) for i in input().rstrip()] for _ in range(row)]
    return (row, column, graph)


def break_wall_and_move(row, column, graph):
    visited = [[0] * column for _ in range(row)]
    visited_broken = [[0] * column for _ in range(row)]
    queue = deque([(0, 0, 1, 1)])
    visited[0][0] = 1
    x_change = [1, -1, 0, 0]
    y_change = [0, 0, 1, -1]

    is_path_exist = False
    while queue:
        current_state = queue.popleft()
        x_position = current_state[0]
        y_position = current_state[1]
        number_of_moves = current_state[2]
        wall_breakable = current_state[3]

        if x_position == row - 1 and y_position == column - 1:
            is_path_exist = True
            break

        for i in range(4):
            x_position_new = x_position + x_change[i]
            y_position_new = y_position + y_change[i]
            if wall_breakable == 1:
                if 0 <= x_position_new <= row-1 and 0 <= y_position_new <= column-1 and graph[x_position_new][y_position_new] == 0 and visited[x_position_new][y_position_new] == 0:
                    queue.append([x_position_new, y_position_new,
                                  number_of_moves+1, wall_breakable])
                    visited[x_position_new][y_position_new] = 1
                elif 0 <= x_position_new <= row-1 and 0 <= y_position_new <= column-1 and graph[x_position_new][y_position_new] == 1 and wall_breakable == 1 and visited[x_position_new][y_position_new] == 0:
                    queue.append(
                        [x_position_new, y_position_new, number_of_moves+1, 0])
                    visited[x_position_new][y_position_new] = 1
            else:
                if 0 <= x_position_new <= row-1 and 0 <= y_position_new <= column-1 and graph[x_position_new][y_position_new] == 0 and visited_broken[x_position_new][y_position_new] == 0:
                    queue.append([x_position_new, y_position_new,
                                  number_of_moves+1, wall_breakable])
                    visited_broken[x_position_new][y_position_new] = 1

    if is_path_exist == True:
        answer = number_of_moves
    else:
        answer = -1
    return answer


main()
