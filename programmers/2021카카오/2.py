# 10진수 -> n진수 변환 함수
# https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95 참고
def transform(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime(n):
    if n == 1:
        return 0

    flag = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            flag = 0
            break

    return flag


def solution(n, k):
    answer = 0
    n_trans = transform(n, k)

    n_list = []
    for w in n_trans:
        if w == '0':
            n_str = ''.join(n_list)
            if n_str and is_prime(int(n_str)):
                answer += 1
            n_list = []
        else:
            n_list.append(w)

    if n_list:
        n_str = ''.join(n_list)
        if n_str and is_prime(int(n_str)):
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
