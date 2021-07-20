# 2020카카오 문자열 압축


def solution(s):
    l_s = len(s)
    l_max = len(s) // 2

    if l_s == 1:
        return 1

    length_list = []
    for i in range(1, l_max + 1):
        res = l_s % i
        length = 0
        word_prev = ""
        count = 0
        for j in range(l_s//i):
            word = s[j*i: j*i+i]
            if word == word_prev:
                count += 1
            else:
                if count <= 1:
                    length += i * count
                else:
                    length += i + len(str(count))
                word_prev = word
                count = 1

        if count <= 1:
            length += i * count
        else:
            length += i + len(str(count))
        length += res
        length_list.append(length)

    answer = min(length_list)
    return answer


print(solution("xxxxxxxxxxyyy"))
