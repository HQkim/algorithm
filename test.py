sudoku, zero = [], []
finish = False

for i in range(9):
    sudoku.append(list(map(int, input().split())))

for i in range(9):                              # 0의 좌표를 리스트 하나에 정리
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i, j])

def alt(a, b):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):                          # 가로열, 세로열에서 이미 사용된 숫자 제거
        if sudoku[i][b] in check:
            check.remove(sudoku[i][b])
        if sudoku[a][i] in check:
            check.remove(sudoku[a][i])
    for i in range(a//3, a//3+1):             # 3x3에서 이미 사용된 숫자 제거
        for j in range(b//3, b//3+1):
            if sudoku[i][j] in check:
                check.remove(sudoku[i][j])
    return check

def s(t):
    global finish
    if finish == True:          # 스도쿠가 끝났을 경우 아무 값도 반환하지 않고 끝내기까지 반복한다.
        return
    if len(zero) == t:
        for i in range(9):
            print(*sudoku[i])
        finish = True           # 스도쿠가 완성될 때마다 출력하지 않도록 하는 장치
        return
    a, b = zero[t]
    for i in alt(a, b):
        sudoku[a][b] = i
        s(t+1)
        sudoku[a][b] = 0        # 만약 스두쿠 완성이 안되면, 0으로 초기화한다. 
                                # 0뿐만 아니라 1~9를 제외한 값을 모두 사용 가능하다. 1~9의 유무만을 확인하기 때문
s(0)