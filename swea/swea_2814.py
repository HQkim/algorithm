# swea 2814 최장 경로
def dfs(i, N):
    visited[i] = 1                  # 정점 방문 표시
    c = 0
    for v in graph[i]:
        if visited[v] == 0:         # 연결된 정점 중 방문하지 않은 정점에 대해
            c = max(c, dfs(v, N))   # 최대 갈 수 있는 거리를 더해주기
    visited[i] = 0                  # 방문 하고 나면 방문 초기화
    return c + 1                    # 자기 자신을 더해서 리턴


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]        # 간선 정보를 담는 인접 리스트

    for _ in range(M):                      # 정보 담기
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [0] * (N+1)
    ans = 0
    for i in range(1, N+1):                 # 각 출발점에 대해 최장길이 dfs로 계산 후 갱신
        ans = max(ans, dfs(i, N))

    print(f'#{tc} {ans}')
