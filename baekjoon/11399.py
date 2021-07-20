# ATM
# 11399번


n = int(input())
P = list(map(int, input().split()))

P.sort()

sum = 0
for i in range(0, n):
    sum += P[i] * (n-i)

print(sum)


# 그리디 알고리즘
# Silver 3
