# swea 1974 스도쿠 검증
def check_sudoku(arr):                                  # 1이면 겹치지 않고 0이면 겹친것
    for i in range(9):                                  # 행, 열 체크
        row_set = set(arr[i])
        col_set = set([r[i] for r in arr])
        if len(row_set) != 9 or len(col_set) != 9:
            return 0

    for i in range(0, 9, 3):                            # 3 x 3 격자 체크
        for j in range(0, 9, 3):
            box = set(arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3])
            if len(box) != 9:
                return 0

    return 1


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {check_sudoku(arr)}')
