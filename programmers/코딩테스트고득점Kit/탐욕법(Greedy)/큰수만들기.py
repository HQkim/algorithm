# 시간 초과
# def solution(number, k): 
#     number_list = [int(i) for i in number]

#     start = 0
#     numbers = []

#     count = 0
#     while True:
#         num_max = max(number_list[start:k+1])
#         ind = number_list.index(num_max)
#         numbers.append(num_max)
#         if ind != 0:
#             k -= ind
#         for i in range(ind+1):
#             del number_list[0]
#         if k == 0:
#             break
#         if count > len(number):
#             break


#     if k == 0:
#         number_final = numbers + number_list
#         answer = ''.join([str(i) for i in number_final])
#     else:
#         number_final = numbers + number_list[k:]
#         answer = ''.join([str(i) for i in number_final])
#     return answer

# print(solution("4177252841", 4))

# 스택을 이용한 풀이(질문란에서 힌트 얻음)

def solution(number, k):

    stack = []

    p = 0
    for i in range(len(number)):
        num = int(number[i])

        if not stack:
                stack.append(num)
        else:
            while True:
                if not stack:
                    stack.append(num)
                    break
                if num <= stack[-1]:
                    stack.append(num)
                    break
                else:
                    stack.pop()
                    k -= 1
                if k == 0:
                    stack.append(num)
                    break         
        p = i
        if k == 0:
            break

    stack_string = [str(i) for i in stack]
    if k == 0:
        answer = ''.join(stack_string + list(number[p+1:]))
    else:
        answer = ''.join(stack_string[:-k])
    
    return answer

print(solution("4177252841", 4))