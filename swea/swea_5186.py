# swea 5186 이진수2
# Programming Advanced 시작하기

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    numbers = []    # 정답을 담은 배열
    count = 0       # 자리수 카운트
    div = 1         # 빼줄 수
    while True:
        if N == 0 or count >= 13:   # N이 0이 되거나 자리수가 13을 넘으면 종료
            break

        div /= 2                    # 빼줄 수를 2로 나누기

        if N >= div:                # N이 빼줄 수보다 크거나 같을 떄
            N -= div
            numbers.append('1')
        else:                       # N이 빼줄 수보다 작을 때
            numbers.append('0')

        count += 1

    if count >= 13:                 # N의 자리수가 13을 넘은 경우
        print(f'#{tc} overflow')
    else:                           # N의 자리수가 12 이내인 경우
        ans = ''.join(numbers)
        print(f'#{tc} {ans}')
