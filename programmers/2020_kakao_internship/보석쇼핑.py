# programmers 2020카카오인턴십 보석쇼핑

def solution(gems):
    n = len(gems)           # gems의 길이
    gems_set = set(gems)    
    m = len(gems_set)       # gems 종류의 개수
    gems_dict = {}          # 구간 안에 포함된 gems 기록

    for gem in gems_set:
        gems_dict[gem] = 0
    

    cnt = 1                 # gems의 개수
    i, j = 0, 0             # 투포인터 시작, 끝점
    gems_dict[gems[0]] = 1
    min_diff = [n-1, 0, n-1]    # 구간의 길이, 시작, 끝점
    while i <= j:
        if cnt < m:             # 현재 구간에 있는 보석의 종류가 전체 종류의 개수보다 적을 경우
            if j < n-1:
                j += 1
                if not gems_dict.get(gems[j]):
                    cnt += 1
                gems_dict[gems[j]] += 1
            else:
                break
        else:                   # 현재 구간에 있는 보석의 종류가 전체 종류의 개와 같은 경우
            diff = j - i
            if diff < min_diff[0]:
                min_diff = [diff, i, j]
            
            if i < n-1:
                gems_dict[gems[i]] -= 1
                if not gems_dict.get(gems[i]):
                    cnt -= 1
                i += 1
                    
    answer = [min_diff[1]+1, min_diff[2]+1]
    return answer
