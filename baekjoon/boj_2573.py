# BOJ 2573 빙산
import sys
from collections import deque


# 언제 빙산이 두 덩어리 이상으로 분리되는지 구하는 함수
def get_when_split(n, m, arr):
    year = 0

    while True:
        num_group = get_number_of_group(n, m, arr)
        if num_group >= 2:
            return year
        if num_group == 0:
            return 0
        year += 1


# 빙산의 그룹(덩어리)의 개수를 구하는 함수
def get_number_of_group(n, m, arr):
    cnt = 0
    visited = [[0]*m for _ in range(n)]

    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j, n, m, arr, visited)
                cnt += 1

    return cnt


# 그룹의 개수를 구하기 위해 bfs
def bfs(x, y, n, m, arr, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while q:
        i, j = q.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if arr[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                else:
                    if arr[i][j]:           # 녹는 부분 처리 (이 부분을 함수로 따로 빼서 해줘도 되나 느려짐)
                        arr[i][j] -= 1      
 

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    ices = [list(map(int, input().rstrip().split())) for _ in range(N)]
    answer = get_when_split(N, M, ices)
    print(answer)