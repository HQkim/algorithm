# Programmers 2022카카오블라인드 파괴되지 않은 건물

def solution(board, skill):
    answer = 0
    row, col = len(board), len(board[0])

    # 누적합 구하기 위한 전단계 : t, r1, c1, r2, c2, degree = 2, 0, 0, 2, 2, n 일때
    '''
    n 0 0 -n
    0 0 0 0
    0 0 0 0
    -n 0 0 n
    '''
    arr = [[0]*col for _ in range(row)]
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        m = 1 if t == 2 else -1
        arr[r1][c1] += degree * m
        if r2 < row-1:
            arr[r2+1][c1] -= degree * m
        if c2 < col-1:
            arr[r1][c2+1] -= degree * m
        if r2 < row-1 and c2 < col-1:
            arr[r2+1][c2+1] += degree * m
    
    # 누적합 계산 1: 행방향으로 누적합 구하기
    for i in range(row):
        for j in range(1, col):
            arr[i][j] += arr[i][j-1]
    
    # 누적합 계산 2: 열방향으로 누적합 구하기
    for j in range(col):
        for i in range(1, row):
            arr[i][j] += arr[i-1][j]
    
    # 최종적으로 board에 계산 더하기
    for i in range(row):
        for j in range(col):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])

## 소감
# 누적합이라는 것을 전에 써본적은 있는것 같은데
# 이렇게 사용해야 하는지는 전혀 생각 못했다.
# 시간복잡도상 생각치 못한 풀이가 필요하다는 것은 직감했는데, 오늘도 하나 배워간다.