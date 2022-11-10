# BOJ 1325 효율적인 해킹
import sys
from collections import deque


def bfs(v):
    visited = [0] * (N + 1)
    q = deque([v])
    visited[v] = 1
    c = 1

    while q:
        now = q.pop()
        for a in graph[now]:
            if not visited[a]:
                visited[a] = 1
                c += 1
                q.append(a)

    return c


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    cnt_max = 1
    answer = []

    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[b].append(a)

    for i in range(1, N + 1):
        cnt = bfs(i)
        if cnt > cnt_max:
            answer = [i]
            cnt_max = cnt
        elif cnt == cnt_max:
            answer.append(i)
    
    answer.sort()
    print(*answer)