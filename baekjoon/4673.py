def selfnum(n):
    return n+sum([int(i) for i in str(n)])


b = []
for i in range(1, 10000):
    x = selfnum(i)
    if x < 10000 and (x not in b):
        b.append(x)

for i in range(1, 10000):
    if i not in b:
        print(i)
