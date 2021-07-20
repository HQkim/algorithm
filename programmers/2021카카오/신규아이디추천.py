import string


def solution(new_id):

    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = list(new_id)
    for i in range(len(new_id)):
        if not(new_id[i] in list(string.ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']):
            new_id[i] = ""
    new_id = list("".join(new_id))

    # 3단계
    temp = new_id.copy()
    if len(new_id) > 1:
        for i in range(1, len(new_id)):
            if new_id[i] == "." and new_id[i-1] == ".":
                temp[i] = ""
    new_id = list("".join(temp))

    # 4단계
    if new_id[0] == ".":
        del new_id[0]
    if len(new_id) > 1:
        if new_id[-1] == ".":
            del new_id[-1]

    # 5단계
    new_id = "".join(new_id)
    if not(new_id):
        new_id = "a"
    new_id = list(new_id)

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            del new_id[-1]

    # 7단계
    if len(new_id) <= 2:
        while True:
            new_id.append(new_id[-1])
            if len(new_id) == 3:
                break

    answer = ''.join(new_id)
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
