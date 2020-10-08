a, b, v = map(int, input().split())

day = (v-a)//(a-b)
p = day * (a-b)
i = 0
while True:
    i += 1
    if i % 2 == 1:
        p += a
        print(i, p)
        day += 1
    else:
        p -= b
        print(i, p)
    if p >= v:
        break

print(day)
