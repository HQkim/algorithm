from collections import deque
t = int(input())

answer_list = []
for _ in range(t):
    n, k = map(int, input().split())
    number_deque = deque(list(input()))

    rotation_number = n // 4

    number_set = set()
    for _ in range(rotation_number):
        end = number_deque.pop()
        number_deque.appendleft(end)

        for i in range(4):
            ind_start = rotation_number*i
            ind_end = rotation_number*(i+1) - 1

            number_hex = ""
            for j in range(ind_start, ind_end+1):
                number_hex += number_deque[j]
            number_set.add(int(number_hex, 16))

    number_list = list(number_set)
    number_list.sort(reverse=True)

    answer_list.append(number_list[k-1])

for i in range(t):
    print(f'#{i+1} {answer_list[i]}')
