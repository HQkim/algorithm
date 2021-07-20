def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(big(i))
    return answer


def big(num):
    org = format(num, "b")
    l_org = len(org)
    if org[-1] == "0":
        result = org[:-1] + "1"
        return int(result, 2)

    org = "0"+org
    stack = []
    for s in org:
        stack.append(s)

    for i in range(l_org, -1, -1):
        if stack[i] == "0":
            print(i)
            stack[i], stack[i+1] = stack[i+1], stack[i]
            break
    result = "".join(stack)

    return int(result, 2)
