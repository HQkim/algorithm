t = int(input())


k_list=[]
n_list=[]
for i in range(t):
    k_list.append(int(input()))
    n_list.append(int(input()))

n_0=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
n_t=[[] for _ in range(14)]

for i in range(14):
    for j in range(14):
        if i==0:
            n = sum(n_0[0:j+1])
            n_t[i].append(n)
        else:
            n = sum(n_t[i-1][0:j+1])
            n_t[i].append(n)

for i in range(t):
    print(n_t[k_list[i]-1][n_list[i]-1])

