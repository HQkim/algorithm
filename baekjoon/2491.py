# 백준 2491 수열

import sys

input = sys.stdin.readline


def longest_sequence(n, arr):
    if n == 1:
        return 1

    ans_list = []

    # 증가하는 수열
    ans = 0
    for i in range(n):
        ans += 1
        if i == n-1 or arr[i] > arr[i+1]:
            ans_list.append(ans)
            ans = 0

    # 감소하는 수열
    ans = 0
    for i in range(n):
        ans += 1
        if i == n-1 or arr[i] < arr[i+1]:
            ans_list.append(ans)
            ans = 0

    return max(ans_list)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(longest_sequence(n, arr))
