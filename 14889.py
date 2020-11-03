import sys

num = int(sys.stdin.readline())

s = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num)]

n, m = num, num//2

check = [False]*(n+1)
a = [0]*m


def go(index, n, m, tot):
    if index == m:
        b = []
        for i in range(1, n+1):
            if check[i] == False:
                b.append(i)

        stat_a = 0
        for i in a:
            for j in a:
                stat_a += s[i-1][j-1]

        stat_b = 0
        for i in b:
            for j in b:
                stat_b += s[i-1][j-1]

        tot.append(abs(stat_a - stat_b))

        return
    for i in range(1, n+1):
        if check[i]:
            continue
        check[i] = True
        if index == 0:
            a[index] = i
            go(index+1, n, m, tot)
        if index > 0 and i > a[index-1]:
            a[index] = i
            go(index+1, n, m, tot)
        check[i] = False


tot = []
go(0, n, m, tot)
print(min(tot))
