def yes_tail(n, ans):
    if n == 1:
        return 1
    return yes_tail(n-1, ans + n)


def no_tail(n):
    if n == 1:
        return 1
    return n + no_tail(n-1)

# 출처: http://melonicedlatte.com/2021/05/10/001900.html
