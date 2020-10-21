t = int(input())

for i in range(t):
    a, word = map(str, input().split())
    a = int(a)
    new_word = word[:a-1] + word[a:]
    print(new_word)
