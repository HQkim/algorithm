# BOJ 1197 최소 스패닝 트리

import sys

# 부모를 찾는 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소의 집합을 합치는 함수
def union(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a <= parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b
 
input = sys.stdin.readline

V, E = map(int, input().split())
parent = list(range(V+1))
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key = lambda x: x[2])    # 정렬을 통해 가장 적은 비용의 경로부터 탐색하게 하기

edge_cnt = 0
total = 0
for edge in edges:
    if edge_cnt == V-1:         # 간선의 개수가 (노드의 개수 - 1)개가 되면 모두 연결
        break
    a, b, c = edge
    if find_parent(a) != find_parent(b):    # 간선 끝의 두 노드의 부모가 다른 경우 합치기
        union(a, b)
        edge_cnt += 1
        total += c
    
print(total)