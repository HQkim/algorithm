# BOJ 9465 스티커

import sys


def calculate_max_point(n, arr):
    answer = 0

    if n == 1:
        answer = max(arr[0][0], arr[1][0])
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        for i in range(2, n):
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
        answer = max(arr[0][n-1], arr[1][n-1])

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = [list(map(int, input().rstrip().split())) for _ in range(2)]
        answer = calculate_max_point(n, arr)
        print(answer)