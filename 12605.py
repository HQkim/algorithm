n = int(input())

for i in range(1,n+1):
    l = input().split()
    l.reverse()
    print("Case #{}: ".format(i), end="")
    for j in l:
        print(j, end=" ")
    print()
