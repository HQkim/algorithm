# BOJ 9019 DSLR

import sys
from collections import deque


def bfs(num_a, num_b):
    visited = [0] * 10000
    visited[num_a] = 1
    q = deque([('', num_a)])

    while q:
        cmd, num = q.popleft()

        num_d = (2 * num) % 10000
        num_s = num - 1 if num > 0 else 9999
        num_l =  num // 1000 + (num % 1000) * 10
        num_r = num // 10 + (num % 10) * 1000

        if not visited[num_d]:
            q.append((cmd + 'D', num_d))
            visited[num_d] = 1
            if num_d == num_b:
                return cmd + 'D'
        if not visited[num_s]:
            q.append((cmd + 'S', num_s))
            visited[num_s] = 1
            if num_s == num_b:
                return cmd + 'S'
        if not visited[num_l]:
            q.append((cmd + 'L', num_l))
            visited[num_l] = 1
            if num_l == num_b:
                return cmd + 'L'
        if not visited[num_r]:
            q.append((cmd + 'R', num_r))
            visited[num_r] = 1
            if num_r == num_b:
                return cmd + 'R'


if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().rstrip().split())
        answer = bfs(A, B)
        print(answer)

