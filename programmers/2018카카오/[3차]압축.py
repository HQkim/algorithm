# programmers 2018카카오블라인드 [3차]압축

def solution(msg):
    answer = []
    d = {}
    for i in range(65, 91):
        d[chr(i)] = i - 64

    num = 27
    w = msg[0]
    while msg:
        msg = msg[1:]
        if msg:
            c = msg[0]
        else:
            c = ''
            
        if w + c in d:
            w = w + c
        else:
            answer.append(d[w])
            d[w+c] = num
            num += 1
            w = c

    if w:
        answer.append(d[w])

    return answer


solution("KAKAO")
solution("TOBEORNOTTOBEORTOBEORNOT")
solution("ABABABABABABABAB")
