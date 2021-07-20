capital = []
for i in range(65, 91):
    capital.append(chr(i))

line = str(input())

for alpha in line:
    if alpha in capital:
        print(alpha, end="")
