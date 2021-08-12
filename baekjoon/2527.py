# 백준 2527 직사각형

import sys

input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    answer = "a"    # 초기값을 "a"로하고 아래 조건들로 거르기
    if x1 > p2 or p1 < x2 or y1 > q2 or q1 < y2:    # 겹치는 부분이 없는 경우
        answer = "d"
    if x1 == p2 or p1 == x2:        # 세로방향으로 봤을 때 꼭지점 or 선분으로 만나는 경우
        if y1 == q2 or q1 == y2:    # 꼭지점
            answer = "c"
        else:                       # 선분
            answer = "b"
    if y1 == q2 or q1 == y2:        # 가로방향으로 봤을 떄 꼭지점 or 선분으로
        if x1 == p2 or p1 == x2:    # 꼭지점
            answer = "c"
        else:                       # 선분
            answer = "b"

    print(answer)

# https://itcrowd2016.tistory.com/85 참고
