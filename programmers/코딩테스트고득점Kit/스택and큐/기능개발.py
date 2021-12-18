# programmers lv2 기능개발
from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = [0]*n

    for i in range(n):                  # 각 기능별 남은 작업 일수
        progress = progresses[i]
        speed = speeds[i]
        quo = (100-progress) // speed
        res = (100-progress) % speed
        day = quo
        if res:
            day += 1
        days[i] = day


    days_q = deque(days)                # 배포되는 기능 개수 계산                
    day_distribute = days_q.popleft()
    count = 1
    
    while days_q:                       
        num = days_q.popleft()

        if num > day_distribute:
            answer.append(count)
            day_distribute = num
            count = 1
        else:
            count += 1
    answer.append(count)

    return answer

solution([93, 30, 55], 	[1, 30, 5]) # answer [2, 1]
solution([95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1]) # answer [1, 3, 2]