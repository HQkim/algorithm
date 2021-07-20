import sys

position = str(sys.stdin.readline())

horizontal = ["a", "b", "c", "d", "e", "f", "g", "h"]

x = horizontal.index(position[0])  # 알파벳 좌표를 숫자 좌표로 변환 0-7
y = int(position[1])-1             # 0-7로 변환


move = []
for i in range(1, 3):
    for j in range(1, 3):
        if i != j:
            move.append([i, j])
            move.append([i, -j])
            move.append([-i, j])
            move.append([-i, -j])

count = 0
for i in move:
    x_new = x + i[0]
    y_new = y + i[1]
    if x_new > -1 and x_new < 8 and y_new > -1 and y_new < 8:
        count += 1

print(count)
