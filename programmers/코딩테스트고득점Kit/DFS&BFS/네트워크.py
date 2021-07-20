from collections import deque

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


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 1, 1]]))

