word_all = []
while True:
    word = str(input())
    if word == "END":
        break
    word_all.append(word)

for word in word_all:
    word_list = list(word)
    word_list.reverse()
    word_reverse = ''.join(word_list)
    print(word_reverse)
