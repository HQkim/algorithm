# swea 1979 어디에 단어가 들어갈 수 있을까
def check_word(arr, n, k):             # 들어갈 수 있는 단어의 개수를 반환하는 함수
    answer = 0

    for i in range(n):
        count = 0                   # 행이 바뀔 때 0으로 초기화
        for j in range(n):
            num = arr[i][j]
            if num == 1:            # 1일 경우 count 증가
                count += 1
                if j == N-1:        # 1인데 마지막 자리인 경우 count와 k가 같은지 체크
                    if count == k:
                        answer += 1
            else:                   # 0일 경우 k와 count가 같은지 체크
                if count == k:
                    answer += 1
                count = 0

    return answer


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_trans = list(map(list, zip(*arr)))                      # 열을 행으로 바꾼 배열

    answer = check_word(arr, N, K) + check_word(arr_trans, N, K)
    print(f'#{tc} {answer}')
