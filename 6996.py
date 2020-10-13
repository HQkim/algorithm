# t = int(input())

# result = []
# for i in range(t):
#     a, b = map(str, input().split())
#     c = [a, b]

#     a_list = list(a)
#     b_list = list(b)

#     a_list.sort()
#     b_list.sort()

#     a_sort = "".join(a_list)
#     b_sort = "".join(b_list)

#     print(a_sort, b_sort)
#     if a_sort == b_sort:
#         count = 0
#     else:
#         count = 1

#     c.append(count)
#     result.append(c)

# for i in result:
#     if i[2] == 0:
#         print("{} & {} are anagrams.".format(i[0], i[1]))
#     else:
#         print("{} & {} are NOT anagrams.".format(i[0], i[1]))


t = int(input())

result = []
for i in range(t):
    a, b = map(str, input().split())
    c = [a, b]

    a_list = list(a)
    b_list = list(b)

    count = 0
    for w in b_list:
        if w in a_list:
            pass
        else:
            count += 1

    print(a_list, b_list)

    c.append(count)
    result.append(c)

for i in result:
    if i[2] == 0:
        print("{} & {} are anagrams.".format(i[0], i[1]))
    else:
        print("{} & {} are NOT anagrams.".format(i[0], i[1]))
