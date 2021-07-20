from sys import stdin
t = int(stdin.readline())

anw = []
for i in range(t):
    h, w, n = map(int, stdin.readline().split())
    m = n // h
    r = n % h
    if r != 0:
        num_1 = str(r)
        if m <= 8:
            num_2 = "0"+str(m+1)
        else:
            num_2 = str(m+1)
    else:
        num_1 = str(h)
        if m <= 9:
            num_2 = "0"+str(m)
        else:
            num_2 = str(m)
    num = num_1 + num_2
    anw.append(int(num))

for l in anw:
    print(l)
