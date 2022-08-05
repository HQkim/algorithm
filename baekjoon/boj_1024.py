# BOJ 1024 수열의 합

N, L = map(int, input().split())

is_p = False
while L < 101:
    res = N - L*(L-1)//2
    if res < 0:
        break
    if res % L == 0:
        x = res // L
        is_p = True
        break
    
    L += 1

if is_p:
    x_list = [i for i in range(x, x+L)]
    print(*x_list)
else:
    print(-1)


# 이건 정말 수학 문제였다
