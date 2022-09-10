# programmers 2019카카오인턴십 징검다리건너기

def check(stones, k, num):
    cnt = 0                 # 건너뛰어야 하는 돌의 수

    for stone in stones:
        if stone < num:     # 건너는 사람의 개수보다 숫자가 작을 때
            cnt += 1
        else:
            cnt = 0
        
        if cnt == k:        # 건너뛰어야 하는 돌의 수가 k가 되면 못건넘
            return False
    
    return True


def solution(stones, k):
    niniz = min(stones)     # 징검다리를 건널 수 있는 니니즈 수의 최소값
    left = niniz            # 탐색할 범위 왼쪽 경계
    right = max(stones)     # 탐색할 범위 오른쪽 경계

    while left <= right:  
        mid = (left + right) // 2

        if check(stones, k, mid):       # mid 만큼 건널 수 있다면
            left = mid + 1              # 최소값을 mid로
            niniz = mid
        else:                           # mid 만큼 건널 수 없다면
            right = mid - 1             # 최대값을 mid로

    return niniz
