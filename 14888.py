import sys


def case(index, n, m, case):
    if index == m:
        seq = []
        for i in range(m):
            seq.append(op[i])
        case.append(seq)
        return

    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        if index == 0:
            a[index] = i
            go(index+1, n, m)
        if index > 0 and i > a[index-1]:
            a[index] = i
            go(index+1, n, m)
        check[i] = False
    pass


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
op_org = list(map(int, sys.stdin.readline().rstrip().split()))

op = []
for i in range(4):
    for j in range(op_org[i]):
        op.append(i)

check = [0] * len(op)


# import sys

# check = [False]*(n+1)
# a = [0]*m


# def go(index, n, m):
#     if index == m:
#         for i in range(m):
#             print(a[i], end=' ')
#         print()

#         return
#     for i in range(1, n+1):
#         if check[i]:
#             continue
#         check[i] = True
#         if index == 0:
#             a[index] = i
#             go(index+1, n, m)
#         if index > 0 and i > a[index-1]:
#             a[index] = i
#             go(index+1, n, m)
#         check[i] = False


# go(0, n, m)
