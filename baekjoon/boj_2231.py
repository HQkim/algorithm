n = int(input())

num = []
for i in range(1, n+1):
    n_sum = i + sum([int(j) for j in str(i)])
    if n_sum == n:
        num.append(i)

if num == []:
    print(0)
else:
    print(min(num))
