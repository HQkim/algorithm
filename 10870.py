def pibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return pibo(n-2)+pibo(n-1)
n = int(input())
print(pibo(n))