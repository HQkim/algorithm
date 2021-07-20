# permutation 사용하면 시간 초과^..^
from itertools import permutations

def solution0(begin, target, words):
    answer = 0

    length = len(words)
    word_len = len(begin)
    a = [i for i in range(length)]
    permute = list(permutations(a, length))

    answer_list = []
    if target in words:
        for p in permute:
            final = ""
            count = 0
            new_bigin = begin
            for i in p:                
                diff = 0
                for j in range(word_len):
                    if new_bigin[j] != words[i][j]:
                        diff += 1
                if diff > 1:
                    break
                count += 1
                new_bigin = words[i]
                if new_bigin == target:
                    answer_list.append(count)
                    break

        answer = min(answer_list)               

    return answer

# 상우가 말해준 bfs 방식으로 풀었을 때
from collections import deque
def solution(begin, target, words):
    answer = 0

    words = deque(words)
    words.appendleft(begin)

    l = len(words)
    l_w = len(begin)

    graph = [[] for _ in range(l)]

    # 그래프 만들기
    for i in range(l):
        for j in range(i+1,l):
            d = 0
            for k in range(l_w):            
                if words[i][k] != words[j][k]:
                    d += 1
            if d == 1:
                print(i,j)
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [-1] * l
    print(graph)

    # bfs로 가장 작은값 찾아내기
    queue = deque([0])
    visited[0] = 0
    queue_2 = []
    distance = 0

    if target in words:
        while queue:
            v = queue.popleft()

            if not queue_2:
                distance += 1
            elif visited[queue_2[-1]] != visited[v]:
                distance += 1
            
            for i in graph[v]:
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = distance
            
            queue_2.append(v)
            if words[v] == target:
                break
        answer = visited[v]

    return answer

print(solution("hit","cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

