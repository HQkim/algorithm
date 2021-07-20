n = int(input())

a = [input() for _ in range(n)]
c = []


for i in range(n):
    b = []
    for j in range(len(a[i])):
        if a[i][j] == "O":
            count = 1
            if j > 0:
                for k in range(j):
                    if a[i][j-(k+1)] == "O":
                        count += 1
                    else:
                        break
        else:
            count = 0
        b.append(count)
    print(sum(b))
