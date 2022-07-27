def d(n):
    return n + sum([int(i) for i in str(n)])

for i in range(1, 10001):
    cnt = 0
    for j in range(max(1, i-len(str(i))*9), i):
        if d(j) == i:
            cnt += 1

    if cnt == 0:
        print(i)
