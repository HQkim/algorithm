k = 65536


def solution(str1, str2):
    str1_list, str1_set = make_set(str1)
    str2_list, str2_set = make_set(str2)

    if not(str1_set) and not(str2_set):
        return k

    set_intersect = str1_set.intersection(str2_set)
    set_union = str1_set.union(str2_set)

    a = 0
    b = 0
    for i in set_intersect:
        a += min(str1_list.count(i), str2_list.count(i))
    for i in set_union:
        b += max(str1_list.count(i), str2_list.count(i))

    answer = int(k*a / b)
    return answer


def make_set(str):
    length = len(str)
    str = str.lower()

    str_list = []
    for i in range(length-1):
        if (97 <= ord(str[i]) <= 122 or 65 <= ord(str[i]) <= 90) and (97 <= ord(str[i+1]) <= 122 or 65 <= ord(str[i+1]) <= 90):
            str_sample = str[i:i+2]
            str_list.append(str_sample)
    str_set = set(str_list)
    return (str_list, str_set)


solution("E=M*C^2", "e=m*c^2")
