import sys

# 테스트케이스의 개수 t
t = int(sys.stdin.readline())

# 길이 리스트 만들기
l_list = []
for i in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    l = y-x
    l_list.append(l)

l_max = max(l_list)
l = 1
s = 1
k = 1
k_list = []

while l < l_max:
    if k == 1:
        k_list.append(l)
    elif k == 2:
        l += s
        k_list.append(l)
    elif k % 2 == 1:
        s += 1
        l += s
        k_list.append(l)
    else:
        l += s
        k_list.append(l)

    k += 1

for l in l_list:
    for i in range(len(k_list)):
        if k_list[i] >= l:
            print(i+1)
            break
