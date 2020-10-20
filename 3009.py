import sys

p = list(list(map(int, sys.stdin.readline().rstrip().split()))
         for _ in range(3))

x_list = []
y_list = []
for i in range(3):
    x_list.append(p[i][0])
    y_list.append(p[i][1])

x_min = min(x_list)
y_min = min(y_list)
x_max = max(x_list)
y_max = max(y_list)

num_xmin = x_list.count(x_min)
num_ymin = y_list.count(y_min)

if num_xmin == 1:
    x = x_min
else:
    x = x_max

if num_ymin == 1:
    y = y_min
else:
    y = y_max

print(x, y)
