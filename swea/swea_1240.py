# swea 1240 1일차 - 단순 2진 암호 코드

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [input() for _ in range(N)]  # 입력받은 배열

    code_dict = {       # 각 암호코드에 해당하는 숫자 딕셔너리
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    for i in range(N):      # graph에서 1이 포함된 행번호 찾기(row)
        if "1" in graph[i]:
            row = i
            break

    for j in range(M-1, -1, -1):    # 1이 포함된 행번호에서 뒤에서부터 1을 찾기(<- 모든 암호코드는 마지막이 1)
        if graph[row][j] == "1":
            col = j
            break

    col_start = col - 8*7 + 1   # 암호가 시작하는 위치 찾기
    even, odd, test = 0, 0, 0  # 짝수, 홀수 자리의 합과 검증코드를 나타내는 변수
    is_valid = True  # 정상적인지 판단하는 플래그

    # 암호코드 숫자를 짝,홀,검증코드 변수에 담기
    for i in range(1, 9):
        num_code = graph[row][col_start+(i-1)*7:col_start+i*7]
        if num_code not in code_dict:   # 암호가 code_dict에 없는 경우 정상적이 않다.
            is_valid = False
            break

        num = code_dict[num_code]
        if i == 8:
            test += num
        elif i % 2 == 0:
            even += num
        else:
            odd += num

    total = odd * 3 + even + test

    if total % 10 != 0:
        is_valid = False

    if is_valid:
        print(f'#{tc} {odd+even+test}')
    else:
        print(f'#{tc} {0}')
