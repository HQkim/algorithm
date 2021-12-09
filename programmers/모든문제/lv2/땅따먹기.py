def solution(land):

    n = len(land)
    for i in range(1, n):
        for j in range(4):
            max_val = 0
            for k in range(4):
                if k != j:
                    max_val = max(max_val, land[i-1][k])
            land[i][j] += max_val

    answer = max(land[n-1])

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))