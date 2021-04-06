# 백준 12852번

n = int(input())

d = [0] * 1000001

# 각 숫자 최소값 정하기
for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])

# 경로 출력하기
while True:
    print(n, end=" ")
    if n == 1:
        break
    if n % 3 == 0 and d[n // 3] < d[n-1]:
        n //= 3
    elif n % 2 == 0 and d[n // 2] < d[n-1]:
        n //= 2
    else:
        n -= 1
