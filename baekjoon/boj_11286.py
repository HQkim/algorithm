# BOJ 11286 절댓값 힙

import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))


# heapq.heappush(heap, (a, b, c))로 하면
# heapq.heappop(heap)을 하면 (a, b, c)순으로 정렬된 순서로 최소값이 나오는것 같다.
# 보통 a로만 정렬된다고 하는데 동작은 위와 같다.
# 공식 문서를 참고해도 별다른 내용이 없었던것 같은데 다시 한번 찾아보자