def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        if number(i):
            answer += i
        else:
            answer -= i

    return answer


def number(num):
    count = 1
    limit = num // 2

    for i in range(1, limit+1):
        if num % i == 0:
            count += 1

    if count % 2 == 0:
        return True
    return False


print(solution(24, 27))
