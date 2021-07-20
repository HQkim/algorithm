import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

name_all = [str(sys.stdin.readline().rstrip()) for _ in range(n+m)]
name_all.sort()

name_both = []
for i in range(n+m-1):
    if name_all[i] == name_all[i+1]:
        name_both.append(name_all[i])

print(len(name_both))
if len(name_both) > 0:
    for name in name_both:
        print(name)
