from collections import deque

def solution(progresses, speeds):
    queue = deque()

    for i in range(len(progresses)):
        quotient = (100 - progresses[i]) // speeds[i]
        remainder = (100 - progresses[i]) % speeds[i]
        if remainder == 0:
            day = quotient
        else:
            day = quotient + 1
        queue.append(day)
    print(queue)    
    
    answer = []
    while queue:
        number = 0
        criteria = queue.popleft()
        number += 1
        while queue:
            if queue[0] <= criteria:
                number += 1
                queue.popleft()
            else:
                break
        answer.append(number)
    
    return answer

print(solution([93,30,55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))