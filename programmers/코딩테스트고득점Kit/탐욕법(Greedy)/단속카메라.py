def solution(routes):
    answer = 0
    check = [0] * len(routes)
    
    routes = sorted(routes, key = lambda x: x[1])

    print(routes)

    while True:
        if sum(check) ==len(check):
            break
        for i in range(len(routes)):
            if check[i] == 0:
                pos = routes[i][1]
                check[i] = 1
                break

        for i in range(len(routes)):
            if check[i] == 0 and routes[i][0] <= pos:
                print(check[i], routes[i][0])
                check[i] = 1
                
        
        print(pos, check)
        
        answer += 1

    return answer
        


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
    

