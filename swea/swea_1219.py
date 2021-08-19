# swea 1219 길찾기

def dfs(s, g, v):
    stack = []
    visited = [0] * v   # 방문 기록용 리스트

    n = s               # n은 현재 방문한 정점
    visited[n] = 1

    while n > -1:

        for w in graph[n]:
            if visited[w] == 0:     # 방문하지 않은 정점일 경우
                stack.append(n)
                n = w
                visited[n] = 1
                if n == g:          # 정점이 도착점(99)일 경우
                    return 1
                break
        else:
            if stack:
                n = stack.pop()
            else:                   # 스택이 비어 있으면 종료
                n = -1
    return 0


T = 10
for _ in range(1, T+1):
    tc, e = map(int, input().split())
    arry = list(map(int, input().split()))
    graph = [[] for _ in range(100)]        # 간선 정보 담을 그래프
    for i in range(e):
        start, end = arry[i*2], arry[i*2+1]
        graph[start].append(end)

    print(f'#{tc} {dfs(0, 99, 100)}')
