# 2020카카오 괄호변환


def solution(p):
    answer = ''


    def my_logic(w):
        # 1. 입력한 문자열이 빈 문자열인 경우, 빈 문자열 반환
        if w == '':
            return w
        # 2. w를 두 "균형잡힌 괄호 문자열" u, v로 분리. u는 더이상 분리 못해야함.
        stack = 0
        for i in range(len(w)):
            if w[i] == '(':
                stack += 1
            else:
                stack -= 1
            
            if stack == 0:
                s = i
                break
        
        u = w[:s+1]
        v = w[s+1:]

        # 3. 문자열 u가 올바른 괄호 문자열인치 체크
        stack = 0
        is_right = True
        for i in range(len(u)):
            if u[i] == '(':
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                is_right = False
                break
        # 3-1 u가 올바른 문자열이라면 v에 대해 1단계부터 수행후 u에 붙여서 반환
        if is_right:
            return u + my_logic(v)
        
        # 4. 문자열 u가 올바른 문자열이 아니라면
        new = '(' + my_logic(v) + ')'
        u_list = [i for i in u[1:-1]]

        for i in range(len(u_list)):
            if u_list[i] == '(':
                u_list[i] = ')'
            else:
                u_list[i] = '('
        
        u = ''.join(u_list)
        new = new + u

        return new


    answer = my_logic(p)

    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))