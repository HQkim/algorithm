# boj 2953 나는 요리사다

max_point = 0
max_ind = 0
for i in range(1, 6):
    point = sum(map(int, input().rstrip().split()))
    if point > max_point:
        max_ind = i
        max_point = point

print(f'{max_ind} {max_point}')
