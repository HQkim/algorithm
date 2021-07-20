a = [int(input()) for _ in range(10)]

b = [i % 42 for i in a]
b.sort()

for i in range(10):
    for j in range(i+1, 10):
        if b[i] == b[j]:
            b[j] = 100

count = 0
for i in range(10):
    if b[i] < 100:
        count += 1

print(count)
