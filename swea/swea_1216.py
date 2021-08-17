# swea 1216 회문2

def check_palindrome(n, m, arry):
    for i in range(n):                      # n개의 행과 열에 대해
        for j in range(n-m+1):              # 각각 행과 열에서 순회
            row_word = arry[i][j:j+m]       # 행의 단어 체크
            is_palindrome = True
            for k in range(m//2):
                if row_word[k] != row_word[m-1-k]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return True

            col_word = "".join([arry[k][i] for k in range(j, j+m)])  # 열의 단어 체크
            is_palindrome = True
            for k in range(m//2):
                if col_word[k] != col_word[m-1-k]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return True

    return False


for tc in range(1, 11):
    var_to_gar = int(input())
    arry = [input() for _ in range(100)]

    answer = 1
    for i in range(100, 1, -1):             # 길이 100인 회문부터 찾기 시작
        if check_palindrome(100, i, arry):  # 찾으면 break
            answer = i
            break

    print(f'#{tc} {answer}')
