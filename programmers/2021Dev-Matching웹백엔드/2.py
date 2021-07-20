from collections import deque

print("hi")


def solution(rows, columns, queries):
    answer = []

    # 그래프 생성
    graph = [[0]*(columns+1) for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = (i * columns + j + 1)
    print(graph)

    # 회전 시행
    for rot in queries:
        queue = deque()
        x1, y1, x2, y2 = rot[0], rot[1], rot[2], rot[3]

        for i in range(y1-1, y2-1):
            queue.append(graph[x1-1][i])
        for i in range(x1-1, x2-1):
            queue.append(graph[i][y2-1])
        for i in range(y2-1, y1-1, -1):
            queue.append(graph[x2-1][i])
        for i in range(x2-1, x1-1, -1):
            queue.append(graph[i][y1-1])

        # 가장 작은 숫자
        a = min(queue)
        answer.append(a)

        for i in range(y1-1, y2-1):
            if i == y1-1:
                graph[x1-1][i] = queue.pop()
            else:
                graph[x1-1][i] = queue.popleft()
        for i in range(x1-1, x2-1):
            graph[i][y2-1] = queue.popleft()
        for i in range(y2-1, y1-1, -1):
            graph[x2-1][i] = queue.popleft()
        for i in range(x2-1, x1-1, -1):
            graph[i][y1-1] = queue.popleft()

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
