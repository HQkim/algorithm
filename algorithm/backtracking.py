# 부분 집합의 합
# 백트래킹(가지치기x, 가지치기o) / 비트연산 활용법

def f1(i, N):       # 그냥 모든 경우에 대해 dfs
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
        if s == 10:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i+1, N)
        bit[i] = 1
        f1(i+1, N)


def f2(i, N, s, rs):        # 목표값보다 현재값이 큰 경우와, 절대 도달할 수 없는 경우를 가지치기
    global cnt
    cnt += 1
    if i == N:
        if s == 50:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif s > 50:
        return
    elif s+rs < 50:
        return
    else:
        bit[i] = 0
        f2(i+1, N, s, rs-A[i])
        bit[i] = 1
        f2(i+1, N, s+A[i], rs-A[i])


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10

cnt = 0
# f1(0, 10)
f2(0, 10, 0, sum(A))
print(cnt)

# 비트연산 활용
# for i in range(1, 1<<10):   # i가 한 개의 부분집합 구성을 나타냄
#     s = 0                   # i가 나타내는 부분집합의 합
#     for j in range(10):
#         if i & (1<<j):      # A[j]가 부분집합에 포함된 경우
#             s += A[j]
#     if s == 10:
#         for j in range(10):
#             if i & (1 << j):
#                 print(A[j], end = ' ')
#         print()
