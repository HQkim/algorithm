def nCr(n, r, s, k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(n, r, i+1, k+1)


N = 4
R = N // 2
comb = [0] * R
nCr(N, R, 0, 0)
