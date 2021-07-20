import math

def solution(brown, yellow):
    total = brown + yellow

    # i 는 세로길이
    vertical = 0
    horizontal = 0 
    for i in range(3, int(math.sqrt(total)) + 1 ):

        res = total % i

        
        if res == 0:
            width = total // i
            num_brown = width * 2 + (i-2) * 2
            
            if num_brown == brown and i <= width:
                vertical = i
                horizontal = width
                print(i, width)
                break        

    answer = [horizontal, vertical]
    return answer

print(solution(10, 2))