from collections import deque

def solution(priorities, location):
    
    queue = deque()
    index_queue = deque()

    for i in range(len(priorities)):
        queue.append(priorities[i])
        index_queue.append(i)
    
    order = 0
    while queue:
        priority = queue.popleft()
        ind_priority = index_queue.popleft()
        
        if priority >= max(queue):
            order += 1
            if ind_priority == location:
                break
        else:
            queue.append(priority)
            index_queue.append(ind_priority)

    answer = order
    return answer

a=[]
for i in range(1,10):
    for j in range(10):
        a.append(i)

print(solution(a, 0))