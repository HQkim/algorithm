def solution(s):
    answer = []
    
    s_list = my_parse(s)
    s_len = len(s_list)
    s_list.sort(key = lambda x: len(x))
    
    for i in range(s_len):
        if i == 0:
            new_set = s_list[i].copy()
            answer.append(new_set.pop())
            continue
        
        new_set = s_list[i] - s_list[i-1]
        answer.append(new_set.pop())

    return answer


def my_parse(s):
    s_list = s[1:-1].split('},')
    s_len = len(s_list)
    for i in range(s_len):
        s_list[i] = set(map(int, s_list[i].strip('{').strip('}').split(',')))
    
    return s_list