a, b = map(str, input().split())

size_a = len(a)
size_b = len(b)

total_a = 0
for i in range(len(a)):
    total_a += int(a[i])

total = 0
for j in range(len(b)):
    total += total_a*int(b[j])

print(total)
