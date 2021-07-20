import sys
n = [i for i in str(sys.stdin.readline().strip())]

n = list(map(int, n))

n.sort(reverse=True)

n = list(map(str, n))

result = ""
for i in n:
    result += i

print(int(result))
