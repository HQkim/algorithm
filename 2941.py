# 예제는 답 맞게 나오는데 제출하면 틀림(잘 모르겠다 이유를, 하지만 아래 방법이 훨씬 간단..)
# a = input()

# alpha = ["c=", 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# num = [1, 1, 2, 1, 1, 1, 1, 1]

# count = len(a)

# for i in range(len(alpha)):
#     m = a.count(alpha[i])
#     num[i] = num[i]*m
#     if i == 2:
#         a = a.replace(alpha[i], '!')
#     print(i, m, num[i], a)

# print(count - sum(num))

a = input()

alpha = ["c=", 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    a = a.replace(i, "!")

print(a, len(a))
