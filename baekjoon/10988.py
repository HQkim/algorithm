word = str(input())

word_list = list(word)
word_list.reverse()

word_reverse = ''.join(word_list)

if word == word_reverse:
    print(1)
else:
    print(0)
