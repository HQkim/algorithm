t = int(input())

for i in range(t):
    a, b = map(str, input().split())

    a_list = list(a)
    b_list = list(b)
    a_list.sort()
    b_list.sort()

    count = 0
    if len(a_list) == len(b_list):
        for j in range(len(a_list)):
            if a_list[j] != b_list[j]:
                count += 1
        if count == 0:
            print("{} & {} are anagrams.".format(a, b))
        else:
            print("{} & {} are NOT anagrams.".format(a, b))

    else:
        print("{} & {} are NOT anagrams.".format(a, b))
