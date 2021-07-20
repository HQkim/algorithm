# 백준 11659 구간 합 구하기 4

# https://ywtechit.tistory.com/79를 참고하여 코드를 구현하였다.
# prefix_sum

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
prefix_sum = [0]*(n+1)

temp = 0
for i in range(n):
    temp += number_list[i]
    prefix_sum[i+1] = temp

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])


# 그냥 sum()으로 합을 구해버리면 N,M 이 100,000이라 최대 O(N*M)이기 때문에 시간초과
