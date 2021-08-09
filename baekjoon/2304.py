# 2304 백준 창고 다각형

import sys

input = sys.stdin.readline

n = int(input())

posts = []
for _ in range(n):
    posts.append(tuple(map(int, input().split())))
posts.sort()

max_h = 0
for i in range(n):
    if posts[i][1] > max_h:
        max_h = posts[i][1]

max_list = []
for i in range(n):
    if posts[i][1] == max_h:
        max_list.append(posts[i])

stack_forward = []
stack_backward = []

height = 0
for i in range(n):
    if posts[i][1] > height:
        height = posts[i][1]
        stack_forward.append(posts[i])
    if posts[i][1] == max_h:
        break

height = 0
for i in range(n-1, -1, -1):
    if posts[i][1] > height:
        height = posts[i][1]
        stack_backward.append(posts[i])
    if posts[i][1] == max_h:
        break

area = 0
for i in range(len(stack_forward)-1):
    width = stack_forward[i+1][0] - stack_forward[i][0]
    height = stack_forward[i][1]
    area += width * height

for i in range(len(stack_backward)-1):
    width = stack_backward[i][0] - stack_backward[i+1][0]
    height = stack_backward[i][1]
    area += width * height

if len(max_list) == 1:
    area += max_h
else:
    width = max_list[-1][0] - max_list[0][0]
    area += (width + 1) * max_h

print(area)
