# boj 4673

## 가장 빠른 풀이
def d(n):
    return n + sum([int(i) for i in str(n)])

self_num = set()
all_num = set(range(1, 10001)) 
for i in range(1, 10001):
    self_num.add(d(i))

no_self_num = all_num - self_num
no_self_num = sorted(list(no_self_num))

for i in no_self_num:
    print(i)

## 자신의 selfnum 구할때 유용한 풀이
# def d(n):
#     return n + sum([int(i) for i in str(n)])

# for i in range(1, 10001):
#     cnt = 0
#     for j in range(max(1, i-len(str(i))*9), i):
#         if d(j) == i:
#             cnt += 1

#     if cnt == 0:
#         print(i)
