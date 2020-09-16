import sys
T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{i}: {a} + {b} = {c}".format(i=i+1, a=a, b=b, c=a+b))
