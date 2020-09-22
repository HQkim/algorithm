n = int(input())

count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
    if i >= 100:
        a = i // 100
        b = (i-100*a) // 10
        c = i % 10
        if (b-a) == (c-b):
            count += 1

print(count)
