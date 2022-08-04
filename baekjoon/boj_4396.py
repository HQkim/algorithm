# BOJ 4396 지뢰 찾기

n = int(input())
mines = [input() for _ in range(n)]
check = [input() for _ in range(n)] 
answer = [['.']*n for _ in range(n)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

is_open = False
for i in range(n):
    for j in range(n):
        if mines[i][j] == '*' and check[i][j] == 'x':
            is_open = True
            continue
        
        if check[i][j] == 'x':
            count = 0
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                if 0<=nr<n and 0<=nc<n and mines[nr][nc] == '*':
                    count += 1
            answer[i][j] = str(count)
        

if is_open:
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                answer[i][j] = '*'

for i in range(n):
    print(''.join(answer[i]))
            