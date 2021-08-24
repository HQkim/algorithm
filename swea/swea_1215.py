# swea 1215 회문1
'''
5
CBCABBAC
BBABCCBA
ABCBCCCA
BACCAABB
BCBCACBC
CABACACB
CAAACCAB
CBABACAC
'''


def count_palindrome(arr, k):
    count = 0
    for a in range(8):
        for i in range(8-k+1):
            is_palindrome = True
            for j in range(k//2):
                if arr[a][i+j] != arr[a][i+k-j-1]:
                    is_palindrome = False
                    break
            if is_palindrome:
                count += 1

        for i in range(8-k+1):
            is_palindrome = True
            for j in range(k//2):
                if arr[i+j][a] != arr[i+k-j-1][a]:
                    is_palindrome = False
                    break
            if is_palindrome:
                count += 1
    return count


T = 10
for tc in range(1, T+1):
    k = int(input())
    arr = [input() for _ in range(8)]
    result = count_palindrome(arr, k)

    print(f'#{tc} {result}')
