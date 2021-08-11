# swea 1209 Sum

for _ in range(10):
    tc = int(input())   # Test Case 번호
    arry = [list(map(int, input().split())) for _ in range(100)]    # 숫자 배열 입력

    max_sum = 0     # 열, 행, 대각선 합중 가장 큰값을 나타낼 변수.

    cross_sum_a = 0     # 왼쪽에서 오른쪽으로 가는 대각선의 합을 저장할 변수
    cross_sum_b = 0     # 오른쪽에서 왼쪽으로 가는 대각선의 합을 저장할 변수
    for i in range(100):
        row_sum = 0     # 각 행의 합을 저장
        column_sum = 0  # 각 열의 합을 저장
        for j in range(100):
            row_sum += arry[i][j]
            column_sum += arry[j][i]

        cross_sum_a += arry[i][i]
        cross_sum_b += arry[i][99-i]

        if row_sum > max_sum:
            max_sum = row_sum
        if column_sum > max_sum:
            max_sum = column_sum

    if cross_sum_a > max_sum:
        max_sum = cross_sum_a
    if cross_sum_b > max_sum:
        max_sum = cross_sum_b

    print(f'#{tc} {max_sum}')
