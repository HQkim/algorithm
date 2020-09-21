import time
a = int(input())
b = int(input())
c = int(input())

start = time.time()
n = str(a*b*c)
c1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in n:
    for j in c1:
        if j == int(i):
            c2[j] += 1

for i in range(10):
    print(c2[i])

print(time.time()-start)
