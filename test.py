def DFS(v):
    global ans
    if v==99:
        ans = 1
        return

    visited[v] = 1 

    for w in adj_list[v]:
        if not visited[w]:
            DFS(w)

for _ in range(10):
    tc, N = list(map(int, input().split()))
    road =  list(map(int, input().split))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2 * i]].append(road[2* i + 1])

    visited = [0] * 100
    ans = 0 

    stack = [0]

    while stack:
        curr = stack.pop()

        if curr == 90:
            ans1 = 1
            break

        if visited[curr]: continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    print('#{} {}'.format(tc, ans))