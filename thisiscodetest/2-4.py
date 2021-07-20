# 내가 짠 코드
n, k = map(int, input().split())

count = 0
while(True):
    if n == 1:
        break
    elif n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

""" 
# 1을 한꺼번에 빼는 코드(수가 커졌을 때 일일이 1을 빼면 속도가 느려짐)
n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)
"""
