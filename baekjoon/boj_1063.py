# BOJ 1063 킹
def check_out(x, y):
    if 1<=x<9 and 1<=y<9:
        return 1
    return 0

v = list(range(9))
h = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
actions = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

king, rock, N = input().rstrip().split()
king = [int(king[1]) , h.index(king[0])]    # v, h 순
rock = [int(rock[1]) , h.index(rock[0])]
for _ in range(int(N)):
    act = input().rstrip()
    dv, dh = actions.get(act)
    king_new = [king[0]+dv, king[1]+dh]
    if (king_new[0] == rock[0]) and (king_new[1] == rock[1]):
        rock_new = [rock[0]+dv, rock[1]+dh]
        if check_out(rock_new[0], rock_new[1]):
            rock[0], rock[1] = rock_new[0], rock_new[1]
            king[0], king[1] = king_new[0], king_new[1]
    else:
        if check_out(king_new[0], king_new[1]):
            king[0], king[1] = king_new[0], king_new[1]

print(h[king[1]]+str(v[king[0]]))
print(h[rock[1]]+str(v[rock[0]]))