# boj 2851 슈퍼 마리오

mushrooms = []
for i in range(10):
    mushrooms.append(int(input()))

point = 0
point_list = []
for i in range(10):
    point += mushrooms[i]
    point_list.append((abs(100-point), point))

point_list.sort(key=lambda x: (x[0], -x[1]))
print(point_list[0][1])