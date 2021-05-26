# 4386번 별자리 만들기
# 2021.05.26 이것이코딩테스트다 책 참조하여 품

import sys
import math

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    n = int(input())

    position_arry = []
    for _ in range(n):
        x, y = map(float, input().rstrip().split())
        position_arry.append((x, y))

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            x_diff = (position_arry[i][0]-position_arry[j][0])**2
            y_diff = (position_arry[i][1]-position_arry[j][1])**2
            cost = math.sqrt(x_diff + y_diff)
            cost = round(cost, 6)
            edges.append((cost, i, j))

    edges.sort()
    number_of_nodes = n
    number_of_edges = len(edges)
    answer = 0
    parent = [0] * number_of_nodes

    for i in range(number_of_nodes):
        parent[i] = i

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    print(round(answer, 3))


main()
