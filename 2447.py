# def star(n, pattern_0, s):
#     num = 3*s
#     pattern = [0] * num

#     for i in range(num):
#         if i // (num//3) == 0 or i // (num//3) == 2:
#             pattern[i] = pattern_0[i % (num//3)] * 3
#         elif i // (num//3) == 1:
#             a = [pattern_0[i % (num//3)], " "*(num//3),
#                  pattern_0[i % (num//3)]]
#             pattern[i] = "".join(a)
#     if num == n:
#         return pattern

#     return star(n, pattern, num)


# n = int(input())

# pattern = star(n, ["***", "* *", "***"], 3)


# for i in pattern:
#     print(i)


def star(n, pattern_0, s):
    num = 3*s
    pattern = [[0]*num for _ in range(num)]

    for i in range(num):
        for j in range(num):
            if i // (num//3) == 0 or i // (num//3) == 2:
                pattern[i] = pattern_0[i % (num//3)] * 3
            elif i // (num//3) == 1:
                a = [pattern_0[i % (num//3)], " "*(num//3),
                     pattern_0[i % (num//3)]]
                pattern[i] = "".join(a)
    if num == n:
        return pattern

    return star(n, pattern, num)


n = int(input())

pattern = star(n, ["*"], 1)

for i in pattern:
    print(i)
