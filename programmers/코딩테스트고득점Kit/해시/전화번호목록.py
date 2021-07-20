# def solution(phone_book):

#     num = list(enumerate(phone_book))

#     dic = {string[1]: string[0] for string in num}

#     answer =True
#     breaker = False
#     for k1,v1 in dic.items():
#         for k2,v2 in dic.items():
#             if k2.startswith(k1) and v1 != v2:
#                 breaker = True
#                 break
#         if breaker == True:
#             answer = False
#             break

#     return answer

# print(solution(["12","123","1235","567","88"]))

def solution(phone_book):
    phone_book.sort()
    answer = True
    if len(phone_book) > 1:
        for i in range(len(phone_book)-1):
            if phone_book[i+1].startswith(phone_book[i]):
                answer = False
    else:
        answer = True
    return answer

solution(["12","132","123","1235","567","88"])