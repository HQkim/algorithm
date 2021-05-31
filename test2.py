from collections import deque

word_input = "I love coding"
code_word = "ambc"
arry = [0, 0, 1, 2, 0]


def solution(word_input, code_word, arry):
    answer_list = []
    word_list = deque([])
    for s in word_input:
        word_list.append(s)

    code_queue = deque(code_word)

    for step in arry:
        code = code_queue.popleft()
        code_queue.append(code)
        print(answer_list, word_list, code)
        for i in range(step):
            word = word_list.popleft()
            if word == " ":
                answer_list.append(word)
                word = word_list.popleft()
            answer_list.append(word)
            if code == word:
                break
        answer_list.append(code)

    if word_list:
        answer_list += word_list
    answer = "".join(answer_list)
    print(answer)
    return


solution(word_input, code_word, arry)
