def solution(places):
    answer = []
    place_size = len(places[0])

    def my_logic(place, size):

        d_1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        d_2 = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        d_3 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        for i in range(size):
            for j in range(size):
                # 사람이 아닐시 넘어가기
                if place[i][j] != 'P':
                    continue

                # 상하좌우 사람 있을시 0 리턴
                for dx, dy in d_1:
                    new_i = i + dx
                    new_j = j + dy
                    if 0<=new_i<size and 0<=new_j<size and place[new_i][new_j]=='P':
                        print('상하좌우! ', i, j, new_i, new_j)
                        return 0
                
                # 거리 2인 상하좌우 사람 있고, 파티션 없을시 0 리턴
                for dx, dy in d_2:
                    new_i = i + dx
                    new_j = j + dy
                    if 0<=new_i<size and 0<=new_j<size and place[new_i][new_j]=='P':
                        if dx == 0:
                            dp = (0, dy//2)
                        else:
                            dp = (dx//2, 0)
                        if place[i+dp[0]][j+dp[1]] != 'X':
                            print('상하좌우 2! ', i, j, new_i, new_j)
                            return 0
                
                # 대각선에 사람 있고, 파티션 없을시 0 리턴
                for dx, dy in d_3:
                    new_i = i + dx
                    new_j = j + dy
                    if 0<=new_i<size and 0<=new_j<size and place[new_i][new_j]=='P':
                        if place[new_i][j] != 'X' or place[i][new_j] != 'X':
                            print('대각선! ', i, j, new_i, new_j)
                            return 0
                
        return 1
    
    for place in places:
        answer.append(my_logic(place, place_size))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
