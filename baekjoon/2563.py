# 백준 2563 색종이

N = int(input())

row_list = [0]*N
col_list = [0]*N

for i in range(N):
    col, row = map(int, input().split())
    row_list[i] = row
    col_list[i] = col

row_max = max(row_list)
col_max = max(col_list)

arry = [[0]*(col_max+10) for _ in range(row_max+10)]

for i in range(N):
    row = row_list[i]
    col = col_list[i]

    for a in range(row, row+10):
        for b in range(col, col+10):
            arry[a][b] = 1

total = 0
for i in range(row_max+10):
    total += sum(arry[i])

print(total)
