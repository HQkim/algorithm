import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

if x >= w/2:
    dist_x = w-x
else:
    dist_x = x

if y >= h/2:
    dist_y = h-y
else:
    dist_y = y

print(min(dist_x, dist_y))
