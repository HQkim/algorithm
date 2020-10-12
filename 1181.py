import sys

n = int(sys.stdin.readline())

words = [str(sys.stdin.readline().strip()) for _ in range(n)]

words_sort = sorted(sorted(words), key=lambda x: len(x))

words_only = []
for i in words_sort:
    if i not in words_only:
        words_only.append(i)

for i in words_only:
    print(i)
