# swea 2001 파리퇴치

test_case = int(input())
for test_case_number in range(test_case):
    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]

    number_of_iteration = (n - m) + 1

    max_sum = 0
    for i in range(number_of_iteration):
        for j in range(number_of_iteration):
            region_sum = 0
            for a in range(i, i+m):
                for b in range(j, j+m):
                    region_sum += graph[a][b]
            if region_sum > max_sum:
                max_sum = region_sum

    print(f'#{test_case_number+1} {max_sum}')
