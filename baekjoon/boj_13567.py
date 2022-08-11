# BOJ 13567 로봇
import sys

input = sys.stdin.readline

M, n = map(int, input().rstrip().split())
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
is_v = True
x, y = 0, 0
d_ind = 0
for _ in range(n):
    if d_ind < 0:
        d_ind = 3
    else:
        d_ind = d_ind % 4
    dx, dy = direct[d_ind]

    act, num = input().rstrip().split()
    num = int(num)

    if act == 'MOVE':
        nx = x + dx * num
        ny = y + dy * num
        if 0 <= nx <= M and 0 <= ny <= M:
            x = nx
            y = ny
        else:
            is_v = False
            break
    else:
        if num == 0:
            d_ind += 1
        else:
            d_ind -= 1

if is_v:
    print(x, y)
else:
    print(-1)

