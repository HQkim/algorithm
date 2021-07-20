n, m = map(int, input().split())
a = [list(input().split()) for _ in range(n)]

b = []
for mat in a:
    b.append(min(mat))

print(max(b))
