# a = [1, 7, 19, 37, 61]

# for i in range(len(a)):
#     if i > 0:
#         print(a[i]-a[i-1])

n = int(input())

i = 1
t = 0
while True:
    if i == 1:
        t = 1
    else:
        t += 6*(i-1)
    if n <= t:
        break
    i += 1

print(i)
