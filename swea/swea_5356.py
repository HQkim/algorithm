# swea 5356 의석이의 세로로 말해요

T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    arr_length = [len(row) for row in arr]  # 각 단어의 길이정보를 담은 배열
    max_length = max(arr_length)            # 길이정보 배열의 최대값

    answer = ''
    for i in range(1, max_length+1):        # 최대값만큼 순회
        word = ''
        for j in range(5):
            if arr_length[j] >= i:          # 각 단어의 길이가 현재 체크하는 길이보다 크거나 같을 때
                word += arr[j][i-1]
        answer += word

    print(f'#{tc} {answer}')
