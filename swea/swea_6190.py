# swea 6190 정곤이의 단조 증가하는 수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    
    max_value = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = A[i] * A[j]
            if num <= max_value:                    # 민형님 코드보고 배움
                continue        
                
            num_string = str(num)
            flag = True                             # 단조 증가 수인지 나타내는 플래그
            for k in range(1, len(num_string)):     # 단조 증가 수 체크
                if num_string[k] < num_string[k-1]:
                    flag = False
                    break
            if flag and num > max_value:
                max_value = num

    print(f'#{tc} {max_value}')