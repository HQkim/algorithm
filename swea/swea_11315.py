'''
1
5
o....
.o...
..o..
...o.
.....
'''

# swea 11315 오목 판정
def check_5(a, b, M):
    # 행과 열 체크
    for i in range(M):
        flag_row = 1
        for j in range(M):
            if arr[a+i][b+j] == ".":
                flag_row = 0
                break
        if flag_row:
            return 1
    
        flag_column = 1
        for j in range(M):
            if arr[a+j][b+i] == ".":
                flag_column = 0
                break
        if flag_column:
            return 1

    # 대각선 체크
    flag_diagonal = 1
    for i in range(M):
        if arr[a+i][b+i] == ".":
            flag_diagonal = 0
            break
    if flag_diagonal:
        return 1

    flag_diagonal = 1
    for i in range(M):
        if arr[a+i][b+M-i-1] == ".":
            flag_diagonal = 0
            break
    if flag_diagonal:
        return 1
    
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    M = 5

    answer = "NO"
    flag = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if check_5(i, j, M):
                flag = 1
                answer = "YES"
                break
        if flag == 1:
            break
    
    print(f'#{tc} {answer}')