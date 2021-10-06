def f(n, m, k):
    if n == k:
        print(p)
    else:
        for i in range(m):
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                f(n, m, k+1)
                u[i] = 0


p = [0]*5
arr = [1, 2, 3, 4, 5]
u = [0]*5
f(5, 5, 0)
