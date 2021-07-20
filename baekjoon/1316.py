n = int(input())
count = 0

for i in range(n):
    c = []
    char = list(input())
    for j in range(len(char)):
        if j == 0:
            c.append(char[j])
        elif char[j] == char[j-1]:
            continue
        elif not(char[j] in c):
            c.append(char[j])
        else:
            count -= 1
            break
    count += 1

print(count)
