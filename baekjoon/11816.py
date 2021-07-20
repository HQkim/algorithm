a = list(str(input()))

num_16 = ["a", 10, "b", 11, "c", 12, "d", 13, "e", 14, "f", 15]

if len(a) >= 2 and a[0] == "0" and a[1] == "x":
    a.reverse()
    num = 0

    for i in range(len(a)-2):
        if a[i] in num_16:
            ind = num_16.index(a[i])
            a[i] = num_16[ind+1]
        num += int(a[i])*16**i

elif a[0] == "0":
    a.reverse()
    num = 0

    for i in range(len(a)-1):
        num += int(a[i])*8**i

else:
    a.reverse()
    num = 0
    for i in range(len(a)):
        num += int(a[i])*10**i

print(num)
