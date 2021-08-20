def dfs(v):
    global ans
    if v == 99:
        ans = 1
        return

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


T = 10
for tc in range(1, T+1):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * 100

    for i in range(n):
        a, b = arr[i*2: (i+1)*2]
        graph[a].append(b)

    ans = 0
    dfs(0)

    print(f'#{tc} {ans}')
