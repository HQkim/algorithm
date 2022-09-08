# programmers 2021카카오 광고삽입

# 문자열 시간을 초(정수)로 바꾸는 함수
def time_to_sec(time):
    time_split = list(map(int, time.split(':')))
    time_sec = time_split[0]*3600 + time_split[1]*60 + time_split[2]
    return time_sec


# 초(정수)를 문자열 시간으로 바꾸는 함수
def sec_to_time(sec):
    h = sec // 3600
    sec = sec % 3600
    m = sec // 60
    s = sec % 60

    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)
    s = '0' + str(s) if s < 10 else str(s)
    
    return h + ':' + m + ':' + s


# 정답 실행 함수
def solution(play_time, adv_time, logs):
    answer = ''
    
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    play_cnt_list = [0] * play_time_sec


    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)
        play_cnt_list[start_sec] += 1
        if end_sec + 1 <= play_time_sec - 1:
            play_cnt_list[end_sec] -= 1
    
    # 누적 합 계산
    for i in range(1, play_time_sec):
        play_cnt_list[i] += play_cnt_list[i-1]
    
    max_play_cnt = sum(play_cnt_list[:adv_time_sec])
    max_play_cnt_starts = [0]
    play_cnt = sum(play_cnt_list[:adv_time_sec])


    for i in range(1, play_time_sec-adv_time_sec+1):
        play_cnt = play_cnt - play_cnt_list[i-1] + play_cnt_list[i+adv_time_sec-1]

        if play_cnt == max_play_cnt:
            max_play_cnt_starts.append(i)
        elif play_cnt > max_play_cnt:
            max_play_cnt = play_cnt
            max_play_cnt_starts = [i]

    answer = sec_to_time(max_play_cnt_starts[0])

    return answer

# print(solution("0:00:06", "00:00:03", ["00:00:00-00:00:03", "00:00:03-00:00:04", "00:00:04-00:00:06"]))
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))