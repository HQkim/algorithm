import sys
from collections import Counter

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for _ in range(n)]

num.sort()

# 평균 구하기
mean = int(round(sum(num)/len(num), 0))

# 중앙값 구하기
ind_med = len(num)//2
median = num[ind_med]

# 범위 구하기
ran = num[len(num)-1]-num[0]

# 최빈값 구하기(여러개 있을 때에는 최빈값 중 두 번째로 작은 값 출력)
cnt = Counter(num)
cnt_mode = cnt.most_common()

if len(cnt_mode) == 1:
    mode = cnt_mode[0][0]
elif cnt_mode[0][1] == cnt_mode[1][1]:
    mode = cnt_mode[1][0]
else:
    mode = cnt_mode[0][0]

print(mean)
print(median)
print(mode)
print(ran)
