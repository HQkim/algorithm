# 1966번 프린터큐

import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

answer_list = []
for _ in range(test_case):
    number_of_documents, target_document = map(int, input().rstrip().split())
    priority_list = list(enumerate(map(int, input().rstrip().split())))

    queue = deque(priority_list)

    print_count = 0

    while queue:
        index, priority = queue.popleft()
        if not queue:
            print_count += 1
            answer_list.append(print_count)
            break
        sorted_queue = sorted(queue, key=lambda x: x[1], reverse=True)
        priority_max = sorted_queue[0][1]
        if priority < priority_max:
            queue.append((index, priority))
            continue
        print_count += 1
        if index == target_document:
            answer_list.append(print_count)
            break

for p in answer_list:
    print(p)
