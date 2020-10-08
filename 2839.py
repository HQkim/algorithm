n = int(input())

r1 = n // 5

if n % 5 == 0:
    r = r1
    print(r)
else:
    candidate = []
    for i in range(r1+1):
        n2 = n - i*5
        if n2 % 3 == 0:
            r2 = n2//3
            r = i + r2
            candidate.append(r)
    if len(candidate) == 0:
        print(-1)
    else:
        print(min(candidate))
