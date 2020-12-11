# 제로
# 10773번
import sys
k = int(sys.stdin.readline().rstrip())

number_list = []
for i in range(k):
    number = int(sys.stdin.readline().rstrip())
    if number != 0:
        number_list.append(number)
    else:
        number_list.pop()
        # del(number_list[-1]) # pop이 빠르다.

print(sum(number_list))


# 다시 한번 느끼지만 input()은 정말 느리고 sys.stdin.readline()은 정말 빠르다.
# 스택
# 실버4
