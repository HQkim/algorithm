# swea 4012 요리사

import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input())
answer_list = []
for _ in range(T):
    N = int(input())
    S_list = [list(map(int, input().split())) for _ in range(N)]

    food_set = set(range(N))
    food_split_combinations = list(combinations(food_set, N//2))

    case_answer_list = []
    for food_set_a in food_split_combinations:
        food_set_a = set(food_set_a)
        food_set_b = food_set - food_set_a

        food_set_a_s = 0
        for i in food_set_a:
            for j in food_set_a:
                food_set_a_s += S_list[i][j]

        food_set_b_s = 0
        for i in food_set_b:
            for j in food_set_b:
                food_set_b_s += S_list[i][j]

        case_answer_list.append(abs(food_set_a_s-food_set_b_s))

    answer_list.append(min(case_answer_list))

for i, number in enumerate(answer_list, start=1):
    print(f'#{i} {number}')
