# programmers 양과 늑대
def solution(info, edges):
    answer = 0
    N = len(info)
    children = [[] for _ in range(N)]   # 각 노드의 자식 노드들 기록
    for edge in edges:
        p, c = edge
        children[p].append(c)
    
    def dfs(sheep, wolf, now):
        if info[now]:   # 늑대 더해주기
            wolf += 1
        else:           # 양 더해주기
            sheep += 1
        
        if sheep <= wolf:   # 양의 개수가 늑대 개수보다 작거나 같아지면 종료
            return 0

        max_sheep = sheep   

        for p in path:              # 탐색 시작
            for n in children[p]:   # 탐색 가능한 경로들 모두 탐색
                if n not in path:   # 경로에 없다면
                    path.append(n)
                    max_sheep = max(max_sheep, dfs(sheep, wolf, n)) # 해당 노드를 방문했을 때, 얻을 수 있는 양의 개수와 비교
                    path.pop()
        
        return max_sheep
        
    path = [0]
    answer = dfs(0, 0, 0)

    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))