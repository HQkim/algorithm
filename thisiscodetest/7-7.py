import time


n = int(input())

array = set(map(int, input().split()))

m = int(input())

x = list(map(int, input().split()))

start = time.time()
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print(time.time() - start)
