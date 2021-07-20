word = str(input())

t = len(word)//10
d = len(word) % 10

if t < 1:
    print(word)
elif d == 0:
    for i in range(t):
        print(word[i*10:(i+1)*10])
else:
    for i in range(t):
        print(word[i*10:(i+1)*10])
    print(word[10*t:])
