from collections import deque

## bfs
def solution(n, computers):
    answer = 0

    visited = [False] * n
    queue = deque()
    
    c = 0

    for i in range(n):
        queue.append(i)
        print(i)
        if not visited[i]:
            print(visited, queue)
            answer += 1
            while queue:
                v = queue.popleft()

                for j in range(n):
                    if computers[v][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
        else:
            queue.popleft()

    return answer

## dfs
def solution2(n, computers):

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
    
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 1, 1]]))

