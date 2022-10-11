# BOJ 2583 영역 구하기
from collections import deque

# 영역의 넓이를 구해주는 함수
def bfs(y, x):
    q = deque([(i, j)])
    graph[i][j] = 1
    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<M and 0<=nx<N and not graph[ny][nx]:
                cnt += 1
                graph[ny][nx] = 1
                q.append((ny, nx))

    return cnt


if __name__ == '__main__':
    M, N, K = map(int, input().rstrip().split())
    graph = [[0]*N for _ in range(M)]
    answer = []

    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().rstrip().split())
        for j in range(min(x1, x2), max(x1, x2)):
            for i in range(min(y1, y2), max(y1, y2)):
                graph[i][j] = 1

    for i in range(M):
        for j in range(N):
            if not graph[i][j]:
                cnt = bfs(i, j)
                answer.append(cnt)

    answer.sort()

    print(len(answer))
    print(*answer)
