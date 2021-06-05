# 백준 1021번 회전하는큐

import sys
import copy
from collections import deque

input = sys.stdin.readline


def solution_a():
    n, m = map(int, input().rstrip().split())
    wanted_arry = deque(list(map(int, input().rstrip().split())))
    number_arry = deque([i for i in range(1, n+1)])

    answer = 0
    while wanted_arry:
        target = wanted_arry.popleft()

        temp_two_arry = copy.deepcopy(number_arry)
        temp_three_arry = copy.deepcopy(number_arry)

        times_two = 0
        times_three = 0
        while True:
            p = temp_two_arry.popleft()
            if p == target:
                break
            temp_two_arry.append(p)
            times_two += 1
        while True:
            if temp_three_arry[0] == target:
                temp_three_arry.popleft()
                break
            p = temp_three_arry.pop()
            temp_three_arry.appendleft(p)
            times_three += 1
        if times_two <= times_three:
            answer += times_two
            number_arry = temp_two_arry
        else:
            answer += times_three
            number_arry = temp_three_arry

    print(answer)
    return

def solution_b():
    n, m = map(int, input().rstrip().split())
    dq = [i for i in range(1, n+1)]
    find_list = list(map(int, input().strip().split()))
    
    answer = 0
    for i in find_list:
        ind = dq.index(i)
        answer += min(len(dq[ind:]), len(dq[:ind]))
        dq = dq[ind+1:] + dq[:ind]
    print(answer)
    return

solution_a()
solution_b()