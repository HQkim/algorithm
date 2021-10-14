def show():
    for i in range(N):
        print(arr[i], end=' ')
    print()


def f1(lev, M):
    if lev == N:
        show()
        return
    for i in range(1, 7):
        arr[lev] = i
        f1(lev+1, M)


def f2(lev, M, start):
    if lev == N:
        show()
        return
    for i in range(start, 7):
        arr[lev] = i
        f2(lev+1, M, i)


def f3(lev, M):
    if lev == N:
        show()
        return
    for i in range(1, 7):
        if not visited[i]:
            visited[i] = 1
            arr[lev] = i
            f3(lev+1, M)
            visited[i] = 0


N, M = map(int, input().split())

arr = [0]*N
visited = [0] * 7

if M == 1:
    f1(0, M)
elif M == 2:
    f2(0, M, 1)
else:
    f3(0, M)
