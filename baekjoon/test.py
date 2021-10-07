def f(i, N):
    global ans
    if i == N:
        ans += 1
        return

    for x in range(N):
        if visited[i] == -1:
            visited[i] = x
            is_valid = True
            for j in range(i):
                if x == visited[j] or abs(visited[j]-x) == abs(i-j):
                    is_valid = False
                    break
            if is_valid:
                f(i+1, N)
            visited[i] = -1


N = int(input())
visited = [-1]*N
ans = 0
f(0, N)

print(f'{ans}')
