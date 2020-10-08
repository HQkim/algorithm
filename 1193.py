import time
x = int(input())

s = time.time()

t = 2
n = 1
i = 1
while True:
    n = (i*(i+1))/2
    if x == 1:

        break
    elif n >= x:
        t = i+1
        n = ((i-1)*(i))/2
        break
    i += 1

while True:
    if t == 2:
        a = 1
        b = 1
    elif t % 2 != 0:
        for i in range(1, t):
            n += 1
            a = i
            b = t-a
            if n == x:
                break
    else:
        for i in range(t-1, 0, -1):
            n += 1
            a = i
            b = t-a
            if n == x:
                break
    if n == x:
        print("{}/{}".format(a, b))
        break

    t += 1

print("{0:5.12}".format(time.time() - s))
