import time

a, b, c = map(int, input().split())
start = time.time()

if c-b > 0:
    n = a // (c-b)
    print(n+1)
else:
    print(-1)

print(time.time()-start)
