# swea 1242 암호코드 스캔

# 출처 : https://tothefullest08.github.io/algorithm/2019/07/21/5_1242_%EC%95%94%ED%98%B8%EC%BD%94%EB%93%9C%EC%8A%A4%EC%BA%94/
# 코드가 너무나 꼬여서 인터넷 상의 코드를 해석하는 식으로 과제를 해봤습니다.
# 참고한 코드도 효율성이 떨어지지만 내일 수정할 계획.

Conversion = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',   # 16진수 -> 4자리 2진수
              '4': ' 0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
              'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

decryption = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5,
              '114': 6, '312': 7, '213': 8, '112': 9}   # 암호코드의 비율중 뒤에 3개만 사용(유일하기 때문)


def reduce(c, b, a):        # 굵어진 암호코드를 가장 작게 줄인다.
    min_num = min(c, b, a)    # 이 때 c,b,a는 순서대로 암호코드 비율의 2,3,4번째 값
    c //= min_num
    b //= min_num
    a //= min_num
    return str(c)+str(b)+str(a)


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Scannner = [input() for _ in range(N)]

    Binary_lst = [''] * N   # 새롭게 2진수 코드를 만든다.
    for i in range(N):
        for j in range(M):
            Binary_lst[i] += Conversion[Scannner[i][j]]

    result = []     # 암호코드의 값을 저장할 리스트
    visited = []    # 현재 코드의 중복을 체크할 리스트
    ans = 0         # 최종 결과값
    for y in range(N):
        a = b = c = 0
        for x in range(M*4-1, -1, -1):  # 각 행의 뒤에서부터 탐색
            # 뒤에서 탐색했을 때 첫번째로 1이 나온 경우
            if b == 0 and c == 0 and Binary_lst[y][x] == '1':
                a += 1
            # 1이 나온 이후에 0이 나온 경우
            elif a > 0 and c == 0 and Binary_lst[y][x] == '0':
                b += 1
            # 1과 0이 나온 후에 다시 1이 나온 경우
            elif a > 0 and b > 0 and Binary_lst[y][x] == '1':
                c += 1

            # 1,0,1 패턴으로 나온 후에 0이 나오면 암호코드 찾기
            if a > 0 and b > 0 and c > 0 and Binary_lst[y][x] == '0':
                result.append(decryption[reduce(c, b, a)])
                a = b = c = 0

            # 암호코드의 값을 저장한 리스트의 길이가 8이 되면 유효한 코드인지 확인
            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * \
                    3 + (result[1] + result[3] + result[5]) + result[7]

                if value % 10 == 0 and result not in visited:           # 유효한 코드이고 반복된 적이 없는 코드라면
                    ans += sum(result)

                visited.append(result)
                result = []

    print('#%d %d' % (tc, ans))
