# swea 1206 View

for tc in range(1, 11):
    n = int(input())
    building_heights = list(map(int, input().split()))

    answer = 0
    for i in range(n):
        # 좌로 1,2칸 우로 1,2칸 떨어진 빌딩의 인덱스
        left_1 = i - 1
        left_2 = i - 2
        right_1 = i + 1
        right_2 = i + 2

        height = building_heights[i]    # 현재 검사하는 빌딩의 높이
        height_differences = []     # 현재 빌딩과 좌우 2칸 빌딩들의 높이 차이를 기록하는 리스트

        if left_1 >= 0:     # 좌로 1칸 떨어진 빌딩의 인덱스가 0보다 크거나 같을 때
            if building_heights[left_1] < height:  # 빌딩의 높이가 검사하는 빌딩보다 낮을 때
                height_differences.append(
                    height-building_heights[left_1])  # 리스트에 높이차 삽입
            else:
                continue    # 빌딩의 높이가 검사하는 빌딩보다 높을 때 다음 빌딩으로 검사 넘어감
        if left_2 >= 0:     # 좌로 2칸 떨어진 빌딩(나머지는 같은 논리)
            if building_heights[left_2] < height:
                height_differences.append(height-building_heights[left_2])
            else:
                continue
        if right_1 <= n-1:  # 우로 1칸 떨어진 빌딩의 인덱스가 n-1보다 작거나 같을 때(나머지는 같은 논리)
            if building_heights[right_1] < height:
                height_differences.append(height-building_heights[right_1])
            else:
                continue
        if right_2 <= n-1:  # 우로 2칸 떨어진 빌딩(나머지는 같은 논리)
            if building_heights[right_2] < height:
                height_differences.append(height-building_heights[right_2])
            else:
                continue

        # 좌우로 조망권이 모두 확보 되었을 때 그 중 가장 높이차가 작은 값을 정답에 더해준다.
        answer += min(height_differences)

    print(f'#{tc} {answer}')
