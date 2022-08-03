# programmers 2021 Dev-Matching: 웹 백엔드 개발(상반기) 행렬 테두리 회전하기

# 새로운 풀이
def solution(rows, columns, queries):
    answer = []
    graph = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = [q-1 for q in query]
        rotatings = []
        coordinates = []

        # 회전하는 숫자들 및 좌표 구하기
        for j in range(y1, y2):
            rotatings.append(graph[x1][j])
            coordinates.append((x1, j))
        for i in range(x1, x2):
            rotatings.append(graph[i][y2])
            coordinates.append((i, y2))
        for j in range(y2, y1, -1):
            rotatings.append(graph[x2][j])
            coordinates.append((x2, j))
        for i in range(x2, x1, -1):
            rotatings.append(graph[i][y1])
            coordinates.append((i, y1))
        
        answer.append(min(rotatings))

        # 회전시켜서 값 바꾸기
        rotatings = [rotatings[-1]]+rotatings[:len(rotatings)-1]
        for i in range(len(rotatings)):
            x, y = coordinates[i]
            graph[x][y] = rotatings[i]

    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]])

''' 시험 당시 풀이
from collections import deque

def solution(rows, columns, queries):
    answer = []

    # 그래프 생성
    graph = [[0]*(columns+1) for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = (i * columns + j + 1)

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
'''