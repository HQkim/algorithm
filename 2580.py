# 2580
# 스도쿠

import sys

def sudoku

check = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        num = check[i][j]
        if num == 0:
            a = i // 3
            b = j // 3
            num_list = []
            for l in range(a*3, a*3+3):
                for m in range(b*3, b*3+3):
                    num_list.append(check[l][m])
            for k in range(1,10):
                if k not in check[i] and k not in [x[j] for x in check] and k not in num_list:
                    check[i][j] = k

for i in range(9):
    for j in range(9):
        print(check[i][j], end=" ")
    if i != 8:
        print()