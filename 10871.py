import sys
N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range(len(A)):
    if A[i] < X:
        print(A[i], end=" ")
