# BOJ 1074 Z

## 재귀로 짠 코드
def recur(n, r, c):
    if n == 0:
        return 0
    d = 2**(n-1)
    return d**2 * (2*(r//d) + (c//d)) + recur(n-1, r%d, c%d)


N, r, c = map(int, input().split())
print(recur(N, r, c))


## for문으로 짠 코드
# N, r, c = map(int, input().split())

# z_order = [(0, 0), (0, 1), (1, 0), (1, 1)]
# cnt = 0
# for i in range(N, 0, -1):
#     d = 2**(i-1)
#     x = r // d
#     y = c // d

#     for j in range(4):
#         if x == z_order[j][0] and y == z_order[j][1]:
#             res = (d**2) * j
#     cnt += res
#     r -= x * d
#     c -= y * d

# print(cnt)