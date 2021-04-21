# 1920번

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input().rstrip())
n_list = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
m_list = list(map(int, input().rstrip().split()))

n_list.sort()

def binary_serach(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_serach(array, target, start, mid - 1)
    else:
        return binary_serach(array, target, mid+1, end)

for i in m_list:
    if binary_serach(n_list, i, 0, n-1) == None:
        output(str(0)+"\n")
    else:
        output(str(1)+"\n")

