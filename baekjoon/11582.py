import copy

n = int(input())

store = list(map(int, input().split()))

store_copy = copy.deepcopy(store)

k = int(input())

num = 2
while True:
    store_new = []
    for i in range(n):
        if i % num == 0:
            store_frac = store_copy[i:i+num]
            store_frac.sort()
            for j in store_frac:
                store_new.append(j)

    p = n / num
    if n/num == k:
        break
    num *= 2

for i in store_new:
    print(i, end=" ")
