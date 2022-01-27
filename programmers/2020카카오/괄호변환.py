# 2020카카오 괄호변환


def solution(p):
    answer = ''

    def split(w):
        # 빈 문자열이라면 그대로 리턴
        if w == '':                    
            return w

        # 균형잡힌 괄호 문자열 u, v로 분리
        num_stack = 0
        split_num = len(w)

        for i in range(len(w)):
            if w[i] == '(':
                num_stack += 1
            else:
                num_stack -= 1

            if num_stack == 0:
                split_num = i
                break

        u = w[:split_num+1]
        v = w[split_num+1:]

        # u가 올바른 괄호 문자열인지 확인
        num_stack = 0
        is_valid = True
        for i in range(len(u)):
            if u[i] == '(':
                num_stack += 1
            else:
                num_stack -= 1
            
            if num_stack < 0:
                is_valid = False
                break
        
        
        if is_valid:                # u가 올바른 괄호 문자열이라면
            u += split(v)
            return u
        else:                       # u가 올바른 괄호 문자열이 아니라면
            word = '(' + split(v) + ')' 
            new_u = u[1:-1]
            append_u = ''
            for i in range(len(new_u)):
                if new_u[i] == ')':
                    append_u += '('
                else:
                    append_u += ')'
            
            word += append_u
            return word
    
    answer = split(p)

    return answer

print(solution("(()())()"))