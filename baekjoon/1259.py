
word_all = []
while True:
    word = str(input())

    if word == "0":
        break

    word_all.append(word)

for word in word_all:
    word_list = list(word)
    word_list.reverse()
    word_reverse = ''.join(word_list)

    if word == word_reverse:
        print("yes")
    else:
        print("no")
