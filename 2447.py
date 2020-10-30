# sol1) 메모리 초과 -> 아래와 코드 같은데 초기값 문제 (n = 3일때 무한 재귀)
def star(n, pattern_0, s):
    num = 3*s
    pattern = [0] * num

    for i in range(num):
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

pattern = star(n, ["***", "* *", "***"], 3)

for i in pattern:
    print(i)


# # sol2) 정답
# def star(n, pattern_0, s):
#     num = 3*s
#     pattern = [0]*num

#     for i in range(num):
#         if i // (num//3) == 0 or i // (num//3) == 2:
#             pattern[i] = pattern_0[i % (num//3)] * 3
#         elif i // (num//3) == 1:
#             a = [pattern_0[i % (num//3)], " "*(num//3),
#                     pattern_0[i % (num//3)]]
#             pattern[i] = "".join(a)
#     if num == n:
#         return pattern

#     return star(n, pattern, num)


# n = int(input())

# pattern = star(n, ["*"], 1)

# for i in pattern:
#     print(i)

# <<교훈>>
# + 로 string 을 하는 것은 메모리를 많이 사용한다. join을 이용하는게 메모리를 적게 사용한다.