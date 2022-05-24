def solution(n, info):
    answer = [0] * 11
    temp = [0] * 11
    diff_max = 0

    def back(n, ind):
        nonlocal diff_max

        # 종료 조건
        if n < 0:
            return

        if ind < 0:
            diff = 0
            for i in range(11):
                if temp[i] > info[i]:
                    diff += 10-i
                elif info[i]:
                    diff -= 10-i
            
            if diff > diff_max:
                for i in range(11):
                    answer[i] = temp[i]
                answer[10] += n
                diff_max = diff

            return

        # 이기는 경우
        temp[ind] = info[ind] + 1
        back(n-temp[ind], ind-1)
        temp[ind] = 0
        
        # 지는 경우
        back(n, ind-1)
        return
    
    back(n, 10)

    if diff_max > 0:
        return answer

    return [-1]

solution(5, [2,1,1,1,0,0,0,0,0,0,0])