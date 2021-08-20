def solution(s):
    answer = ''
    number_str = set(str(i) for i in range(10))  # 숫자 set
    # 숫자 대응 영단어 dictionary
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    stack = []  # 영소문자 쌓이는 stack
    for i in s:
        if i in number_str:  # 문자가 숫자면 그대로 출력
            answer += i
            continue  # 다음 문자로 이동
        stack.append(i)  # 숫자가 아니면 stack에 추가
        word = "".join(stack)  # stack으로 단어 구성
        if dic.get(word):  # 단어가 dictionary에 있을 때 변환해서 추가 & stack 비우기
            answer += dic[word]
            stack.clear()

    return int(answer)


print(solution("one4seveneight"))
