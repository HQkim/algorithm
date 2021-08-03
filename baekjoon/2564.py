# 백준 2564 경비원

import sys

input = sys.stdin.readline

width, height = map(int, input().split())
number_of_stores = int(input())

where_list = []  # 서,북,동,남 순으로 하나의 리스트 만든다고 했을때 상점 및 동근이 index 기록
for _ in range(number_of_stores+1):  # 동근이 위치도 넣어줄 것이므로 +1 해줌
    # 북남서동을 나타내는 direction, 얼마나 떨어져 있는지 나타내는 distance
    direction, distance = map(int, input().split())
    if direction == 1:  # 북
        ind_total = height + distance  # 북쪽은 서쪽 지나서 계산
    elif direction == 2:  # 남
        # 남쪽은 서,북,동,남 지난 것에서 distance 빼기
        ind_total = 2 * (height + width) - distance
    elif direction == 3:  # 서
        ind_total = height - distance  # 서쪽은 바로 계산
    else:  # 동
        ind_total = height + width + distance  # 동쪽은 서,북 지나고 계산
    where_list.append(ind_total)

ind_security = where_list.pop()  # 동근이의 위치

result = 0  # 최단거리 합 정의 및 초기화
total_length = 2 * (width + height)  # 사각형 전체 길이
for ind in where_list:  # ind는 상점의 위치(index)
    if ind_security == ind:
        continue
    elif ind_security > ind:
        result += min((total_length - ind_security) + ind,
                      ind_security - ind)  # 시계방향, 반시계 방향 중 작은 값
    else:
        result += min(ind - ind_security, ind_security +
                      (total_length - ind))  # 시계방향, 반시계 방향 중 작은 값

print(result)
