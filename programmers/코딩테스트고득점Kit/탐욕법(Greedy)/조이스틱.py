def solution(name):
    name = list(name)

    n = len(name)

    current_name = ["A"]*n

    answer = 0
    p = 0

    while True:
        print(current_name)
    
        # 현재 위치에서 알파벳 비교후 변경
        answer += min(ord(name[p])-ord("A"), ord("Z")-ord(name[p])+1)    
        current_name[p] = name[p]

        # 변경 후 current_name = name 이라면 break
        if current_name == name:
            break

        # 변경 후 current_name != name 이라면 이동

        # 오른쪽 이동
        p_r = p
        c_r = 0
        while True:
            p_r += 1
            c_r += 1
            if current_name[p_r] != name[p_r]:
                break

        # 왼쪽으로 이동
        p_l = p
        c_l = 0
        while True:
            p_l -= 1
            c_l += 1
            if current_name[p_l] != name[p_l]:
                break

        if c_r <= c_l:
            p += c_r
            answer += c_r
        else:
            p -= c_l
            answer += c_l

    return answer