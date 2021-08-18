import sys

input = sys.stdin.readline


def check_win_1(a_list, b_list):
    star_a = a_list.count(4)
    circle_a = a_list.count(3)
    square_a = a_list.count(2)
    triangle_a = a_list.count(1)
    star_b = b_list.count(4)
    circle_b = b_list.count(3)
    square_b = b_list.count(2)
    triangle_b = b_list.count(1)

    if star_a > star_b:
        return "A"
    elif star_a < star_b:
        return "B"

    if circle_a > circle_b:
        return "A"
    elif circle_a < circle_b:
        return "B"

    if square_a > square_b:
        return "A"
    elif square_a < square_b:
        return "B"

    if triangle_a > triangle_b:
        return "A"
    elif triangle_a < triangle_b:
        return "B"

    return "D"


def check_win_2(a_list, b_list):  # 어 위는 112ms였다가 이건 144ms? 왜 더느리지 ㅋㅋ
    a_list.sort()
    b_list.sort()
    a_win = False
    b_win = False

    while a_list and b_list:
        a = a_list.pop()
        b = b_list.pop()
        if a > b:
            a_win = True
            break
        elif a < b:
            b_win = True
            break

    if a_win:
        return "A"
    elif b_win:
        return "B"
    elif a_list:
        return "A"
    elif b_list:
        return "B"
    else:
        return "D"


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, *ai = list(map(int, input().split()))
        b, *bi = list(map(int, input().split()))

        print(check_win_2(ai, bi))
