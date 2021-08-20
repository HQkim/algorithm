def solution(places):
    answer = []

    num = 0
    for place in places:
        # 배열로 변환
        graph = [[] for _ in range(5)]
        for i in range(5):
            graph[i] = [a for a in place[i]]

        # P인곳 찾기
        p_list = []
        for i in range(5):
            for j in range(5):
                if graph[i][j] == "P":
                    p_list.append((i, j))

        # 거리두기 체크
        check = 1
        while p_list:
            if len(p_list) == 1:
                break
            pos = p_list.pop()
            Flag = True
            for p in p_list:
                r_diff = pos[0] - p[0]
                c_diff = pos[1] - p[1]
                dis = abs(r_diff) + abs(c_diff)
                if dis == 1:  # 거리 1인 경우 거리두기 x
                    Flag = False
                    break
                if dis > 2:  # 거리 2초과시 거리두기 o
                    continue
                if r_diff == 0:  # 거리 2이고 같은 행에 있을 시
                    if graph[p[0]][p[1]+c_diff-1] == "X":
                        continue
                    Flag = False
                    break
                if c_diff == 0:  # 거리 2이고 같은 열에 있을 시
                    if graph[p[0]+r_diff-1][p[1]] == "X":
                        continue
                    Flag = False
                    break
                # 거리 2이고 대각선에 있을 시
                if graph[p[0]+r_diff][p[1]] == "X" and graph[p[0]][p[1]+c_diff] == "X":
                    continue
                Flag = False
                break

            if Flag == False:
                check = 0
                break
        num += 1
        answer.append(check)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                               "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
