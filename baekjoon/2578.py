import sys

input = sys.stdin.readline


def check_bingo(arry):
    count = 0

    cross_sum_a = 0
    cross_sum_b = 0
    for i in range(5):
        if sum(arry[i]) == 0:
            count += 1

        column = [row[i] for row in arry]
        if sum(column) == 0:
            count += 1
        cross_sum_a += arry[i][i]
        cross_sum_b += arry[i][4-i]

    if cross_sum_a == 0:
        count += 1
    if cross_sum_b == 0:
        count += 1

    if count >= 3:
        return True
    else:
        return False


if __name__ == "__main__":
    my_arry = [list(map(int, input().split())) for _ in range(5)]

    host_arry = []
    for i in range(5):
        host_arry += list(map(int, input().split()))

    for i in range(25):
        number = host_arry[i]

        for j in range(5):
            for k in range(5):
                if my_arry[j][k] == number:
                    my_arry[j][k] = 0

        if check_bingo(my_arry):
            answer = i + 1
            break

    print(answer)
