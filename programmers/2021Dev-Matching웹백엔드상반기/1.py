def solution(lottos, win_nums):
    answer = []

    c = 0
    for i in win_nums:
        if i in lottos:
            c += 1

    zero = lottos.count(0)

    best = c + zero
    worst = c

    answer.append(win(best))
    answer.append(win(worst))

    return answer


def win(n):
    if n == 6:
        a = 1
    elif n == 5:
        a = 2
    elif n == 4:
        a = 3
    elif n == 3:
        a = 4
    elif n == 2:
        a = 5
    else:
        a = 6

    return a


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
