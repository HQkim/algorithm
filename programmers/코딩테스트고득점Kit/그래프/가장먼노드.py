from collections import deque

def solution(n, edge):
    
    nodes = [999999] * (n+1)
    nodes[0], nodes[1] = 0, 0
    
    graph = [[] for _ in range(n+1)]

    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    print(graph)

    queue = deque([1])
    visited = [-1] * (n+1)
    visited[1] = 0

    distance = 0
    queue_2 = []
    while queue:
        v = queue.popleft()

        print(queue, visited, v)

        if not queue_2:
            distance += 1      
        elif visited[queue_2[-1]] != visited[v]:
            distance += 1
            
        for i in graph[v]:
            if visited[i]==-1:
                queue.append(i)
                visited[i] = distance

        queue_2.append(v)
        
    answer = visited.count(max(visited))
    print(visited)
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))