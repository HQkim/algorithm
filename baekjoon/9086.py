t = int(input())

sen = []
for i in range(t):
    a = list(input())
    if len(a)==1:
        print(a[0]+a[0])
    else:
        print(a[0]+a[-1])

