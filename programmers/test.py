# 2020카카오 문자열 압축

def solution(s):
    answer = 1000
    s_len = len(s)

    if s_len == 1:
        return 1

    for c in range(1, s_len//2+1):
        s_comp = '' # 압축한 문자열
        count = 0   # 반복된 횟수
        k = ''      # 중복되는 문자열
        for i in range(0, s_len, c):
            if not k:
                k = s[i:i+c]
                count += 1
                continue

            if i+c < s_len:
                now = s[i:i+c]
            else:
                now = s[i:]

            if now == k:
                count += 1
            else:
                if count == 1:
                    s_comp += k
                else:
                    s_comp += str(count)+k
                k = now
                count = 1

        if count == 1:
            s_comp += k
        else:
            s_comp += str(count)+k

        answer = min(answer, len(s_comp))

    return answer


print(solution("xababcdcdababcdcd"))

