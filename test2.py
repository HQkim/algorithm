import math

T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())

    z = (4*(x+y))**2 - 4*12*x*y
    h = (4*(x+y)-math.sqrt(z))/24
    v = h * (x-2*h) * (y - 2*h)

    print('#{0} {1:.6f}'.format(tc, v))