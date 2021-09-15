# boj_1004 어린 왕자

import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    n = int(input())

    start_set = set()   # 어린왕자를 포함하는 원의 집합
    end_set = set()     # 장미를 포함하는 원의 집합

    for i in range(n):
        cx, cy, r = map(int, input().rstrip().split())
        d1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        d2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if d1 < r or math.isclose(d1, r):   # 어린왕자를 포함하는 경우
            start_set.add(i)
        if d2 < r or math.isclose(d2, r):   # 장미를 포함하는 경우
            end_set.add(i)

    result_set = (start_set | end_set) - (start_set & end_set)  # 합집합에서 교집합 빼주기

    print(len(result_set))
