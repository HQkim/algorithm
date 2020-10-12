t = int(input())

result = []
for i in range(t):
    a, b = map(int, input().split(","))
    plus = a+b
    result.append(plus)

for i in result:
    print(i)
