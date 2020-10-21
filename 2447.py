def star1(n, pattern_0, s):
    num = 3*s
    pattern = [0] * num
    i = 0
    for i in range(num):
        if i // (num//3) == 0 or i // (num//3) == 2:
            pattern[i] = pattern_0[i % (num//3)] * 3
        elif i // (num//3) == 1:
            a = [pattern_0[i % (num//3)], " "*(num//3),
                 pattern_0[i % (num//3)]]
            pattern[i] = "".join(a)
    if num == n or num == 81:
        return pattern

    return star1(n, pattern, num)


def star2(n, pattern_0, s):
    num = 3*s
    pattern = [0] * num
    i = 0
    for i in range(num):
        if i // (num//3) == 0 or i // (num//3) == 2:
            pattern[i] = pattern_0[i % (num//3)] * 3
        elif i // (num//3) == 1:
            a = [pattern_0[i % (num//3)], " "*(num//3),
                 pattern_0[i % (num//3)]]
            pattern[i] = "".join(a)
    if num == n:
        return pattern

    return star2(n, pattern, num)


n = int(input())

pattern = star1(n, ["***", "* *", "***"], 3)
if len(pattern) != n:
    pattern = star2(n, pattern, 81)

for i in pattern:
    print(i)
