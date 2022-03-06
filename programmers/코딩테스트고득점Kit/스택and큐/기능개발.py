# programmers lv2 기능개발

def solution(progresses, speeds):
    answer = []
    p_len = len(progresses)
    work_day = [0] * p_len

    for i in range(p_len):
        day = (100-progresses[i]) // speeds[i]
        left = (100-progresses[i]) % speeds[i]
        if left:
            day += 1
        work_day[i] = day

    local_max = work_day[0]
    count = 1
    for i in range(1, p_len):
        if work_day[i] > local_max:
            answer.append(count)
            local_max = work_day[i]
            count = 1
        else:
            count += 1
    
    answer.append(count)

    return answer

solution([93, 30, 55], 	[1, 30, 5]) # answer [2, 1]
solution([95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1]) # answer [1, 3, 2]