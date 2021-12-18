# programmers lv2 주식가격

def solution(prices):
    n = len(prices)
    answer = [1] * n
    
    answer[-1] = 0
    for i in range(n-2, -1, -1):
        if prices[i] <= prices[i+1]:
            answer[i] += answer[i+1]

    print(answer)

solution([1, 2, 3, 2, 3])