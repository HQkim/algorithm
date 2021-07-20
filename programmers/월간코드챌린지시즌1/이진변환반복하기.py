def solution(s):
    answer = [0, 0]

    count = 0
    while True:
        s_length = len(s)
        if s_length == 1:
            break

        s_one_count = list(s).count("1")
        s_zero_count = s_length - s_one_count
        s = bin(s_one_count)[2:]
        count += 1
        answer[1] += s_zero_count

    answer[0] = count
    print(answer)

    return answer


solution("110010101001")
