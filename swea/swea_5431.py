# swea 5431 민석이의 과제 체크하기

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    student_submit = list(map(int, input().split()))
    student_lazy = [0] * (N+1)
    for i in student_submit:
        student_lazy[i] = 1
    print(f'#{tc}', end=" ")
    for i in range(1, N+1):
        if student_lazy[i] == 0:
            print('{}'.format(i), end=" ")
    print()
