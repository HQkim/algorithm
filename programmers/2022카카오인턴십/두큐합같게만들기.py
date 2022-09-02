# pro 두 큐 합 같게 만들기

def solution(queue1, queue2):
    answer = -1
    q = queue1 + queue2     # 두 개의 큐를 이어 붙이기
    q = q*2                 # 큐를 두배로 복사하기
    n = len(queue1)

    total = sum(queue1) + sum(queue2)
    if total % 2 != 0:
        return answer
    
    goal = total // 2
    start, end = 0, n-1
    sum_q1 = sum(q[start: end+1])
    

    # 투포인터 방식으로 문제 풀이
    while 1:
        if sum_q1 == goal:                          # 두 큐의 합이 같은 경우
            answer = (start - 0) + (end - (n - 1))
            break
        
        if sum_q1 < goal:                           # 첫번째 큐의 합이 작은 경우
            if end + 1 < 4*n:                       # 끝점을 한칸 뒤로, 범위 벗어나면 종료
                end += 1
                sum_q1 += q[end]
            else:
                break
        
        if sum_q1 > goal:                           # 첫번째 큐의 합이 큰 경우
            if start + 1 <= end and start + 1 < 2*n:    # 시작점을 한칸 뒤로, 범위 벗어나면 종료
                sum_q1 -= q[start]
                start += 1
            else:
                break

    return answer



print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 10, 1, 2], [1, 2, 1, 2]))