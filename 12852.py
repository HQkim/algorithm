n = int(input())

d = [0] * 1000001


for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])

while True:
    print(int(n), end=" ")
    if n == 1:
        break

    if n % 3 == 0 and d[int(n//3)] <= d[int(n-1)]:
        n /= 3
    elif n % 2 == 0 and d[int(n//2)] <= d[int(n-1)]:
        n /= 2
    else:
        n -= 1
