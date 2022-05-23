def solution(n, computers):

    answer = 0
    visited = [0] * n

    def dfs(x):
        nonlocal n
        print(x)

        for i in range(n):
            if visited[i] == 0 and computers[x][i] == 1:
                visited[i] = 1
                dfs(i)
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            answer += 1

    return answer
