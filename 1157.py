s = str(input())
s = s.lower()
print(type(s))
print(s)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = []
for i in a:
    c.append(s.count(i))
mymax = max(c)
cnt = c.count(mymax)
if cnt > 1:
    print("?")
else:
    anw = a[c.index(mymax)]
    print(anw.upper())
