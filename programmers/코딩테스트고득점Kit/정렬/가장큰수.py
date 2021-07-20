def solution(numbers):
    
    new_array = change_to_comparable(numbers)
    combine_array = combine(new_array, numbers)
    
    result_array = sorted(combine_array, key = lambda x: x[0], reverse=True)
    print(result_array)
    
    answer = ''
    for i in range(len(result_array)):
        answer += str(result_array[i][1])
    return answer

def combine(array_1, array_2):
    array = []
    for i in range(len(array_1)):
        array.append([array_1[i], array_2[i]])
    return array

def change_to_comparable(array):
    new_array = []
    #int to string
    for i in array:
        new_array.append(str(i))
    
    print(new_array)
    
    #change to comparable
    for i in range(len(new_array)):
        if new_array[i] == '0':
            pass
        elif len(new_array[i]) == 1:
            new_array[i] += new_array[i]*2
        elif len(new_array[i]) == 2:
            new_array[i] += str(float(new_array[i][0])-0.5)
        elif len(new_array[i]) == 4:
            new_array[i] = str(0.5)

    #change to int
    for i in range(len(new_array)):
        new_array[i] = float(new_array[i])
        
    return new_array

numbers = [3, 34, 343]

print(solution(numbers))

