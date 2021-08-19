# swea 4408 자기 방으로 돌아가기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 200                    # 복도의 개수
    for _ in range(N):
        a, b = map(int, input().split())
        if a <= b:
            start = (a-1) // 2
            end = (b-1) // 2
        else:
            start = (b-1) // 2
            end = (a-1) // 2

        for i in range(start, end+1):       # 학생이 지나가는 복도에 개수 증가
            corridor[i] += 1

    print(f'#{tc} {max(corridor)}')         # 가장 많이 지나간 복도만큼 시간 필요
