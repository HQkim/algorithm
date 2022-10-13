# BOJ 1389 케빈 베이컨의 6단계 법칙

INF = int(10e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_s = INF
min_v= 1
for i in range(1, N + 1):
    s = sum(graph[i][1:])
    if s < min_s:
        min_s = s
        min_v = i
        
print(min_v)
