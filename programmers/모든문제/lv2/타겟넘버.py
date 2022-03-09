# programmers lv2 타겟 넘버

def solution(numbers, target):
    answer = 0
    n_len = len(numbers)

    def back_track(ind, total, n_len):
        nonlocal answer, target
        if ind == n_len:
            if total == target:
                answer += 1
            return 
        
        if total + sum(numbers[ind:]) < target:
            return
        
        back_track(ind+1, total+numbers[ind], n_len)
        back_track(ind+1, total-numbers[ind], n_len)
    
    back_track(0, 0, n_len)

    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))