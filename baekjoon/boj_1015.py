# boj_1015 수열 정렬

N = int(input())
A = list(map(int, input().split()))

B = sorted(A)

for i in range(N):
    ind = B.index(A[i])
    print(ind, end=" ")
    B[ind] = -1
