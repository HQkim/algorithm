# programmers 2018카카오블라인드 [3차]n진수 게임

def solution(n, t, m, p):
    # n진법의 숫자의 나열을 t*m 길이만큼 미리 구하기
    num = 0
    num_n = ''
    while len(num_n) < t * m:
        num_n += convert_to_n(num, n)
        num += 1

    # 순서 p 에 해당하는 숫자만 뽑아내기
    answer = ''.join([num_n[p+i*m-1] for i in range(t)])
    print(answer)

    return answer


def convert_to_n(x, n):    
    if x == 0:
        return '0'

    r_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    result = ''
    while x:
        r = x % n
        if r >= 10:
            r = r_dict[r]
        result = str(r) + result
        x //= n

    return result

solution(2, 4, 2, 1)
solution(16, 16, 2, 1)
solution(16, 16, 2, 2)