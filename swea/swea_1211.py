# swea 1211 Ladder2

T = 10
for _ in range(1, T+1):
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    min_count = 100**2
    min_ind = 0
    for x in range(100):
        if graph[0][x] == 1:
            i = 0
            j = x
            cnt = 0
            while i < 100:
                cnt += 1
                left = j - 1
                right = j + 1
                if left >= 0 and graph[i][left] == 1:       # 왼쪽에 1이 나온다면 왼쪽으로 이동
                    for p in range(left-1, -1, -1):
                        j = p
                        cnt += 1
                        if p-1 == -1 or graph[i][p-1] == 0:
                            break
                    i += 1
                    cnt += 1
                elif right < 100 and graph[i][right] == 1:  # 오른쪽에 1이 나온다면 오른쪽으로 이동
                    for p in range(right, 100):
                        j = p
                        cnt += 1
                        if p+1 == 100 or graph[i][p+1] == 0:
                            break
                    i += 1
                    cnt += 1
                else:                                       # 이외는 아래로 이동
                    i += 1

            if cnt <= min_count:
                min_count = cnt
                min_ind = x

    print(f'#{tc} {min_ind}')