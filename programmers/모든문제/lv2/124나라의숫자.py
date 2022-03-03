# 프로그래머스 lv2 124 나라의 숫자

def solution(n):
    answer = ''

    while n:
        if not n % 3:
            answer += '4'
            n //= 3
            n -= 1
        else:
            answer += str(n % 3)
            n //= 3
        
    answer = answer[::-1]

    return answer

solution(10)