# programmers 2021Dev-Matching웹백엔드상반기 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    d = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    answer = []
    win_nums = set(win_nums)
    cnt_min = 0
    for num in lottos:
        if num in win_nums:
            cnt_min += 1
    
    zero_cnt = lottos.count(0)
    cnt_max = cnt_min + zero_cnt
    answer = [d[cnt_max], d[cnt_min]]

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
