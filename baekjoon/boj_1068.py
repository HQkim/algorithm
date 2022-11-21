# BOJ 1068 트리
import sys

def dfs(t):
    parents[t] = -2
    for i in range(N):
        if parents[i] == t:
            dfs(i)


def count_leaf():
    cnt = 0
    for i in range(N):
        if parents[i] != -2 and i not in parents:
            cnt += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    parents = list(map(int, input().rstrip().split()))
    target = int(input())

    dfs(target)
    answer = count_leaf()

    print(answer)