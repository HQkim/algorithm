# 백준 1655 가운데를 말해요

import sys
import heapq

input = sys.stdin.readline


def solution():
    number_of_integers = int(input())

    max_heap = []
    min_heap = []

    for _ in range(number_of_integers):
        integer = int(input())

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-integer, integer))
        else:
            heapq.heappush(min_heap, (integer, integer))

        if min_heap and max_heap[0][1] > min_heap[0][1]:
            max_of_max_heap = heapq.heappop(max_heap)[1]
            min_of_min_heap = heapq.heappop(min_heap)[1]
            heapq.heappush(min_heap, (max_of_max_heap, max_of_max_heap))
            heapq.heappush(max_heap, (-min_of_min_heap, min_of_min_heap))

        print(max_heap[0][1])
    return


solution()
