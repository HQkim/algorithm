def fibo1(n):
    global cnt1
    cnt1 += 1
    if n >= 2 and len(memo1) <= n:
        memo1.append(fibo1(n-1) + fibo1(n-2))
    return memo1[n]


def fibo2(n):
    global cnt
    cnt += 1
    if n >= 2 and memo2[n] == 0:  # 아직 계산되지 않은 값이면
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]


n = 20

memo1 = [0, 1]
cnt1 = 0
print(fibo1(n), cnt1)

memo2 = [0] * (n+1)
memo2[0] = 0
memo2[1] = 1
cnt = 0
print(fibo2(n), cnt)
