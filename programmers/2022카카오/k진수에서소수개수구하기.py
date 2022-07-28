# 2022카카오블라인드 k진수에서 소수 개수 구하기

def solution(n, k):
    num_k = convert_to_k(n, k)
    numbers = num_k.split('0')

    count = 0
    for num in numbers:
        if num and check_prime(int(num)):   # num을 check하는 이유는 split과정에서 ''와 같은 공백문자가 들어오기 때문
            count += 1
    return count

# 10진법 -> k진법으로 변환
def convert_to_k(n, k):
    result = []
    while n:
        result.append(n % k)
        n //= k

    return ''.join(map(str,result[::-1]))

# 소수인지 체크
def check_prime(n):
    if n == 1:
        return False
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False

    return is_prime
