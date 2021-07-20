import math
from itertools import permutations

def solution(numbers):
    # 정답 array
    ans = [0]*10**(len(numbers))

    # 소수 판별 array
    prime_array = prime_number(len(numbers))
    
    num_list = []
    for i in numbers:
        num_list.append(i)

    num_list_all = []
    for i in range(1, len(num_list)+1):
        num_list_all += list(permutations(num_list,i))

    for word_list in num_list_all:
        word = ""
        for j in word_list:
            word += j
        num = int(word)
        if prime_array[num]==True:
            ans[num] = 1

    answer = sum(ans)
    return answer

# 소수 배열 리턴
def prime_number(l):    
    n = 10**l
    array = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    array[0], array[1] = False, False

    return array

print(solution("17"))
