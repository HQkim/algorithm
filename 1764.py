n, m = map(int, input().split())

name_l = [str(input()) for _ in range(n)]
name_s = [str(input()) for _ in range(m)]

name_both = []
for name in name_l:
    if name in name_s:
        name_both.append(name)

name_both.sort()

print(len(name_both))
for name in name_both:
    print(name)
