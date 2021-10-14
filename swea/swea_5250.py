# swea 5251 최소 이동 거리
# programming advanced/그래프의 최소 비용문제
'''
1
3
0 2 1
0 1 1
1 1 1
'''
import heapq

INF = int(10e9)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 전체 배열의 크기
    H = [list(map(int, input().split())) for _ in range(N)]  # 높이 정보를 다음 2차원 배열

    distance = [[INF]*N for _ in range(N)]      # 사용 연료 정보를 담은 2차원 배열

    q = []  # 우선순위 큐를 나타낼 배열
    heapq.heappush(q, (0, 0, 0))    # 이진트리 기반의 최소힙 자료구조를 통해 q에 push
    distance[0][0] = 0              # 출발점의 연료 소비량은 0으로
    while q:
        dist, i, j = heapq.heappop(q)

        if dist > distance[i][j]:       # 큐에서 나온 연료 사용량이 distance에 표시된 연료 사용량보다 크면 continue
            continue

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:   # 우,하,좌,상에 대해
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:         # 배열 안에 존재할 때
                diff = max(0, H[ni][nj]-H[i][j])
                cost = distance[i][j] + diff + 1
                # i,j에서 ni,nj로 가는 비용이 distance에 표시된 사용량보다 작으면
                if cost < distance[ni][nj]:
                    distance[ni][nj] = cost         # distance 갱신 및 큐에 추가
                    heapq.heappush(q, (cost, ni, nj))

    print(f'#{tc} {distance[-1][-1]}')
