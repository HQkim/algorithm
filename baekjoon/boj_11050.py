# boj 11050 이항 계수 1

N, K = map(int, input().split())

n1 = 1
n2 = 1
n3 = 1

for i in range(1, N+1):
    n1 *= i

for i in range(1, N-K+1):
    n2 *= i

for i in range(1, K+1):
    n3 *= i

ncr = n1 // (n2 * n3)

print(ncr)
