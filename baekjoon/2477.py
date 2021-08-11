# 백준 2477 참외밭

import sys

input = sys.stdin.readline

K = int(input())
arry = [list(map(int, input().split())) for _ in range(6)]  # 참외밭 둘레 정보

max_w, ind_w = 0, 0  # 가장 긴 가로변의 길이, arry에서 index값
max_h, ind_h = 0, 0  # 가장 긴 세로변의 길이, arry에서 index값

for i in range(6):
    direction = arry[i][0]
    length = arry[i][1]

    if direction == 1 or direction == 2:
        if length > max_w:
            max_w = length
            ind_w = i
    if direction == 3 or direction == 4:
        if length > max_h:
            max_h = length
            ind_h = i

# 가장 긴 세로변 좌우에 있는 가로변들의 길이차가 뺄 사각형의 가로변
sub_w = abs(arry[(ind_h-1) % 6][1] - arry[(ind_h+1) % 6][1])
# 가장 긴 가로변 좌우에 있는 세로변들의 길이차가 뺄 사각형의 가로변
sub_h = abs(arry[(ind_w-1) % 6][1] - arry[(ind_w+1) % 6][1])

answer = (max_w * max_h - sub_w * sub_h) * K    # (전체 사각형 - 뺄 사각형) x 넓이당 참외개수
print(answer)

# https://itcrowd2016.tistory.com/84 참고
