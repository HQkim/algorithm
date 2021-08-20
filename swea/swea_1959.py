# swea 1959 두 개의 숫자열
def find_max(list_a, list_b):
    length_a = len(list_a)
    length_b = len(list_b)

    ans = 0
    if length_a >= length_b:
        for i in range(length_a-length_b+1):
            sub_sum = 0
            for j in range(length_b):
                sub_sum += list_a[i+j] * list_b[j]
            if sub_sum > ans:
                ans = sub_sum
    else:
        for i in range(length_b-length_a+1):
            sub_sum = 0
            for j in range(length_a):
                sub_sum += list_b[i+j] * list_a[j]
            if sub_sum > ans:
                ans = sub_sum

    return ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    answer = find_max(Aj, Bj)

    print(f'#{tc} {answer}')
