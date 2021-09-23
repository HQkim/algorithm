# swea 1232 사칙연산

def f(v):
    if len(tree[v]) == 1:                           # 숫자인 경우 그대로 리턴
        return tree[v][0]
    else:
        if tree[v][0] == '-':                       # 연산자인 경우 연산 수행
            return f(tree[v][1]) - f(tree[v][2])
        if tree[v][0] == '+':
            return f(tree[v][1]) + f(tree[v][2])
        elif tree[v][0] == '/':
            return f(tree[v][1]) // f(tree[v][2])
        else:
            return f(tree[v][1]) * f(tree[v][2])


T = 10
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        if len(info) == 2:
            tree[int(info[0])] = [int(info[1])]
        else:
            tree[int(info[0])] = [info[1]]+list(map(int, info[2:]))

    ans = f(1)              # 1번 노드부터 계산

    print(f'#{tc} {ans}')
