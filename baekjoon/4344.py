c = int(input())
a = [list(map(int, input().split())) for _ in range(c)]

if c > 1:
    for i in range(c):
        n = a[i][0]
        count = 0
        for j in range(1, n+1):
            avg = sum(a[i][1:n+1])/n
            if a[i][j] > avg:
                count += 1
            frac = (count/n)*100
        print('{0:2.3f}%'.format(frac))

else:
    n = a[0]
    for i in range(1, n+1):
        count = 0
        avg = sum(a[1:n+1])
        if a[i] > avg:
            count += 1
        frac = (count/n)*100
    print('{0:2.3f}%'.format(frac))
