

def solution(grid):
    row_length = len(grid)
    column_length = len(grid[0])
    directions = [[[0, 0, 0, 0] for _ in range(column_length)]
                  for _ in range(row_length)]
    answer = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    def check(i, j):
        case = []
        for d in range(4):
            if directions[i][j][d] == 1:
                continue
            directions[i][j][d] = 1
            dir = d
            count = 1
            ni = i
            nj = j
            while True:
                ni = ni + di[dir]
                nj = nj + dj[dir]

                if ni >= row_length:
                    ni = 0
                elif ni < 0:
                    ni = row_length - 1
                if nj >= column_length:
                    nj = 0
                elif nj < 0:
                    nj = column_length - 1

                if grid[ni][nj] == "R":
                    dir = (dir+1) % 4
                elif grid[ni][nj] == "L":
                    dir -= 1
                    if dir < 0:
                        dir == 3

                if ni == i and nj == j and dir == d:
                    break

                directions[ni][nj][dir] = 1
                count += 1
            case.append(count)

        return case

    if row_length == 1:
        for i in range(column_length):
            arr = check(0, i)
            answer += arr
    else:
        for i in range(row_length):
            for j in range(column_length):
                arr = check(i, j)
                answer += arr

    answer.sort()

    return answer


print(solution(["S"]))
