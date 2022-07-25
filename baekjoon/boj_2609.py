a, b = map(int, input().rstrip().split())

max_div = 1
for i in range(2, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        max_div = i

min_multi = max_div * (a // max_div) * (b // max_div)

print(max_div)
print(min_multi)