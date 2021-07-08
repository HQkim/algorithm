# 백준 1713 후보 추천하기

import sys
from collections import deque

input = sys.stdin.readline


def solution():

    number_of_pictures = int(input())
    number_of_recommends = int(input())
    recommends_sequence = deque(map(int, input().rstrip().split()))
    list_of_pictures = []

    for number in recommends_sequence:
        # 사진틀에 아무것도 없으면 넣기
        if not list_of_pictures:
            list_of_pictures.append([1, number])
            continue

        # 사진틀에 이미 있으면 추천수만 높이기
        is_in_picture = False
        for student in list_of_pictures:
            if student[1] == number:
                student[0] += 1
                is_in_picture = True
                break

        # 사진틀에 이미 있는 경우
        if is_in_picture:
            continue

        # 사진틀에 없는 경우
        if len(list_of_pictures) != number_of_pictures:  # 비어 있는 경우
            list_of_pictures.append([1, number])

        else:  # 비어 있지 않은 경우
            list_of_recommends = []

            for student in list_of_pictures:
                list_of_recommends.append(student[0])

            min_recommends = min(list_of_recommends)
            index_of_min = []

            for i in range(len(list_of_recommends)):
                if list_of_recommends[i] == min_recommends:
                    index = i
                    break

            del list_of_pictures[index]
            list_of_pictures.append([1, number])

    list_of_pictures.sort(key=lambda x: x[1])
    for i in list_of_pictures:
        print(i[1], end=" ")

    return


solution()
