d_0 = [0]*41
d_1 = [0]*41


def fibo_0(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0

    if d_0[n] != 0:
        return d_0[n]

    d_0[n] = fibo_0(n-1) + fibo_0(n-2)
    return d_0[n]


def fibo_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if d_1[n] != 0:
        return d_1[n]

    d_1[n] = fibo_1(n-1) + fibo_1(n-2)
    return d_1[n]


t = int(input())

for k in range(t):
    n = int(input())
    print(fibo_0(n), fibo_1(n))
