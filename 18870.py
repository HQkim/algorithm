# 18870

# # list 이용해서 중복 모두 계산될 때
# n = int(input())
# x_list = list(map(int , input().split()))
# x_enu = list(enumerate(x_list))
# x_enu.sort(key = lambda x: x[1])

# x_p = [0]
# start = 0
# for i in range(1, n):
#     if x_enu[i][1] > x_enu[i-1][1]:
#         start += 1
#     x_p.append(start)

# for i in range(n):
#     x_enu[i] = [x_enu[i], x_p[i]]

# x_enu.sort(key = lambda x: x[0][0])

# print(" ".join(map(str, [x_enu[i][1] for i in range(n)])))

# set와 dictionary 이용해서 중복 이용 안할 때
import sys

input = sys.stdin.readline
input()
x_list = list(map(int, input().split()))

x = dict()
for i,v in enumerate(sorted(set(x_list))):
    x[v] = i

sys.stdout.write(" ".join(map(str, (x[num] for num in x_list))))