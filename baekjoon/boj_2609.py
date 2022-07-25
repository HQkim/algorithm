# boj 2609 최대공약수와 최소공배수

# 유클리드 호제법을 활용한 풀이
def get_gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

a, b = map(int, input().rstrip().split())

gcd = get_gcd(a, b)
lcm = a * b //gcd

print(gcd)
print(lcm)    