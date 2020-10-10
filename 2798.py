n, m = map(int, input().split())
c = list(map(int, input().split()))

num = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = c[i]+c[j]+c[k]
            if s <= m and i != j and j != k and i != k:
                num.append(s)

print(max(num))
