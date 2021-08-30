# swea 1267 작업순서
from collections import deque

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * (V + 1)
    count = [0] * (V + 1)                   # 자기한테 들어오는 경로수
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        count[b] += 1
        graph[a].append(b)

    queue = deque()
    for i in range(1, V+1):                 # 자기한테 들어오는 경로가 없을 경우
        if count[i] == 0:
            queue.append(i)
            visited[i] = 1

    print('#{}'.format(tc), end=" ")
    while queue:
        now = queue.popleft()
        print("{}".format(now), end=" ")
        for i in graph[now]:
            count[i] -= 1
            if not visited[i] and count[i] == 0:    # 방문하지 않았고 자기한테 들어오는 경로가 없을 경우
                queue.append(i)
                visited[i] = 1
    print()

