def solution(answers):
    
    num1 = 0
    num2 = 0
    num3 = 0
    
    pick_1 = [1, 2, 3, 4, 5]
    pick_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pick_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        re_1 = i % 5
        re_2 = i % 8
        re_3 = i % 10
        
        answer = answers[i]
        if answer == pick_1[re_1]:
            num1 += 1
        if answer == pick_2[re_2]:
            num2 += 1
        if answer == pick_3[re_3]:
            num3 += 1
    
    numbers = [num1, num2, num3]
    
    if numbers.count(max(numbers)) ==1:
        return [numbers.index(max(numbers))+1]
    
    numbers = list(enumerate([num1, num2, num3], 1))

    print(numbers)

    numbers = sorted(numbers, key = lambda x: (-(x[1]+1), x[0]))

    print(numbers)

    answer = []
    for i in numbers:
        answer.append(i[0])
        
    return answer

print(solution([1,3,2,4,2,4,4]))