# 백준 2628 종이자르기

import sys

input = sys.stdin.readline

width, height = map(int, input().split())
cut_number = int(input())

height_list = [0, height]
width_list = [0, width]

for i in range(cut_number):
    a, b = map(int, input().split())
    if a == 0:
        height_list.append(b)
    else:
        width_list.append(b)

height_list.sort()
width_list.sort()

height_result = [height_list[i]-height_list[i-1]
                 for i in range(1, len(height_list))]
width_result = [width_list[i]-width_list[i-1]
                for i in range(1, len(width_list))]

print(max(height_result)*max(width_result))

# 내가 짠 코드는 5배쯤 됐었다. 상위권 코드를 참조해서 줄였다.
# 근데 실행속도는 내가 짠 코드와비슷하다.
