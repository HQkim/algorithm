# 동전0
# 11047번 문제


n, k = map(int, input().split())

A = []
for i in range(n):
    A.append(int(input()))

A.reverse()

count = 0
for coin in A:
    if coin <= k:
        quotient = k // coin
        remainder = k % coin
        count += quotient
        k = remainder
        if k == 0:
            break

print(count)

# 소감
# 이건 동전들이 서로 배수여서 간단했는데 배수가 아닌 경우는 단지 큰 수부터 보면
# 안됐던듯. 이거 SSAFY 준비할 때 알고리즘 있었던거 같음.

# 그리디 알고리즘
# Silver 1
