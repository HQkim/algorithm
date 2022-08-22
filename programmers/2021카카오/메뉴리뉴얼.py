from itertools import combinations


def solution(orders, course):
    answer = []

    for num in course:
        d = dict()
        for order in orders:
            if len(order) >= num:
                order_list = list(order)
                comb = list(combinations(sorted(order_list), num))
                for c in comb:
                    word = "".join(c)
                    if word in d:
                        d[word] += 1
                    else:
                        d[word] = 1

        if d:
            if max(d.values()) >= 2:
                max_v = max(d.values())
                answer += [k for k, v in d.items() if v == max_v]

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
