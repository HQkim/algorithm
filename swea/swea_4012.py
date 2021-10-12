from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    food_set = set(range(N))
    # food_set에서 N//2개를 뽑는 경우
    food_combinations = list(combinations(food_set, N//2))

    min_s = int(10e9)
    for set_a in food_combinations:
        set_a = set(set_a)
        set_b = food_set - set_a

        s_a = 0
        for i in set_a:
            for j in set_a:
                s_a += S[i][j]

        s_b = 0
        for i in set_b:
            for j in set_b:
                s_b += S[i][j]

        min_s = min(min_s, abs(s_a-s_b))

    print(f'#{tc} {min_s}')
