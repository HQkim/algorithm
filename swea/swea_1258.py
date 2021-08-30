# swea 1258 행렬찾기
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    boxes = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                row = 1
                col = 1
                for a in range(i+1, n):
                    if arr[a][j] == 0:
                        break
                    row += 1
                for b in range(j+1, n):
                    if arr[i][b] == 0:
                        break
                    col += 1
                boxes.append((row, col, row*col))

                for a in range(i, i+row):
                    for b in range(j, j+col):
                        arr[a][b] = 0

    boxes.sort(key=lambda x: (x[2], x[0]))

    print('#{} {}'.format(tc, len(boxes)), end=" ")
    for box in boxes:
        print('{} {}'.format(box[0], box[1]), end=" ")
    print()