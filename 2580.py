# 2580
# 스도쿠

import sys
input = sys.stdin.readline

graph = [list(map(int, input().rstrip().split())) for _ in range(9)]

zeros = [(i,j) for i in range(9) for j in range(9) if graph[i][j] == 0]

def is_promising(i, j):
    promising = set([1,2,3,4,5,6,7,8,9])

    #행열 검사
    for k in range(9):
        if graph[i][k] in promising:
            promising.remove(graph[i][k])
            if not promising:
                break
        if graph[k][j] in promising:
            promising.remove(graph[k][j])
            if not promising:
                break
    
    #3*3 박스 검사
    i //= 3
    j //= 3
    break_check = 0
    for p in range(i*3, (i+1)*3):
        if break_check == 1:
            break
        for q in range(j*3, (j+1)*3):
            if graph[p][q] in promising:
                promising.remove(graph[p][q])
                if not promising:
                    break_check = 1
                    break
    
    return promising

flag = False #답이 다 나왔는가?
def dfs(x):
    global flag

    if flag:
        return

    if x == len(zeros): # 마지막 0 까지 다 채웠을 경우
        for row in graph:
            print(*row)
        flag = True # 답 다나옴
        return
    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j) # 유망한 숫자 모음

        for num in promising:
            graph[i][j] = num # 유망한 숫자 하나 넣음
            dfs(x + 1) # 다음 0으로 넘어감
            graph[i][j] = 0 # 초기화 (정답이 없을 경우를 대비)

dfs(0)