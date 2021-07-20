import math
t = int(input())

anw = []
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = math.sqrt((x1-x2)**2+(y1-y2)**2)
    r_s = min(r1, r2)
    r_b = max(r1, r2)
    if r == 0:
        if r1 == r2:
            anw.append(-1)
        else:
            anw.append(0)
    else:
        if r > r1+r2:
            anw.append(0)
        elif r == r1+r2:
            anw.append(1)
        elif r < r1+r2:
            if r+r_s < r_b:
                anw.append(0)
            elif r+r_s == r_b:
                anw.append(1)
            else:
                anw.append(2)


for i in anw:
    print(i)
