# programmers 2018카카오 [1차]셔틀버스

from collections import deque

def solution(n, t, m, timetable):
    d = {}
    for time in timetable:
        time_m = time_to_minute(time)
        if d.get(time_m):
            d[time_m] += 1
        else:
            d[time_m] = 1
    
    bus = []
    for i in range(n):
        bus.append(time_to_minute("09:00")+i*t)

    left = 0
    right = 1439
    answer_minute = 0

    def check(time_m):
        if d.get(time_m):
            d[time_m] += 1
        else:
            d[time_m] = 1

        q = []
        for k, v in d.items():
            if k <= time_m:
                q.extend([k]*v)
        q.sort()
        q = deque(q)

        d[time_m] -= 1            

        for b in bus:
            cnt = m
            while cnt:
                if q and q[0] <= b:
                    q.popleft()
                    cnt -= 1
                else:
                    break
        
        if q:
            return False
        else:
            return True
                    

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer_minute = mid
            left = mid + 1
        else:
            right = mid - 1

    answer = minute_to_time(answer_minute)
    return answer


def time_to_minute(time):
    hour, minute = map(int, time.split(':'))
    time_m = hour * 60 + minute
    
    return time_m


def minute_to_time(time_m):
    hour = time_m // 60
    minute = time_m % 60

    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    
    return hour + ":" + minute


# 이분탐색으로 문제를 풀었는데 다른 사람들 풀이를 보니 더 간단한 풀이가 보인다. 추후에 다시 풀어보자.
