import sys
def solution(numbers, target):
    answer = 0
    a = len(numbers)

    def dfs(v):
        plusminus.append(v)
        print(plusminus, numbers)
        if len(plusminus) == a:
            count = 0
            for i in range(a):
                count += plusminus[i] * numbers[i]
            if count == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(1)
            plusminus.pop()
            dfs(-1)
            plusminus.pop()
        

    plusminus = []
    dfs(1)
    plusminus = []
    dfs(-1)

     

    return answer




print(solution([1,1,1,1,1] ,3))