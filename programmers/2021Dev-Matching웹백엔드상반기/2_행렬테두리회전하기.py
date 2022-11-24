# programmers 2021 Dev-Matching: 웹 백엔드 개발(상반기) 행렬 테두리 회전하기
from collections import deque

def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns]+ [[0]+[i*columns+j for j in range(1, columns+1)] for i in range(rows) ]

    for query in queries:
        x1, y1, x2, y2 = query
        q = deque()
        # 회전을 적용할 수들을 q에 담기
        for j in range(y1, y2):
            q.append(graph[x1][j])
        for i in range(x1, x2):
            q.append(graph[i][y2])
        for j in range(y2, y1, -1):
            q.append(graph[x2][j])
        for i in range(x2, x1, -1):
            q.append(graph[i][y1])

        answer.append(min(q))
        
        # 큐를 한칸씩 뒤로 밀기
        q.appendleft(q.pop())

        # 회전시키기
        for j in range(y1, y2):
            graph[x1][j] = q.popleft()
        for i in range(x1, x2):
            graph[i][y2] = q.popleft()
        for j in range(y2, y1, -1):
            graph[x2][j] = q.popleft()
        for i in range(x2, x1, -1):
            graph[i][y1] = q.popleft()
        
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])