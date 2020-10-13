import sys

count = 0
for i in range(8):
    line = list(str(sys.stdin.readline().strip()))
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0 and line[j] == "F":
                count += 1
    else:
        for j in range(8):
            if j % 2 == 1 and line[j] == "F":
                count += 1

print(count)
