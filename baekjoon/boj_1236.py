# BOJ 1236 성 지키기

N, M = map(int, input().split())

visited = [0] * M
count_row = 0
for i in range(N):
    w = input().rstrip()
    is_guard = False
    for j in range(M):
        if w[j] == 'X':
            is_guard = True
            visited[j] = 1
    
    if not is_guard:
        count_row += 1

count_col = sum([1 for v in visited if v == 0])

print(max(count_row, count_col))
