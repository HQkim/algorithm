# 11725번

# 그래프로 풀기

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
result = [0]*(n+1)

for _ in range(n-1):
    i, j = map(int, input().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

stack = [1]
while stack:
    x = stack.pop()
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            result[i] = x
            stack.append(i)

for i in range(2, n+1):
    print(result[i])     


# 좀 이해가 안가는 방식
# import sys
# from collections import deque

# input = sys.stdin.readline

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.child = []
#         self.parent = None

# n = int(input())
# tree = {}
# for i in range(n-1):
#     n1, n2 = map(int, input().rstrip().split())
#     if n1 not in tree:
#         tree[n1] = Node(n1)
#     tree[n1].child.append(n2)
#     if n2 not in tree:
#         tree[n2]=Node(n2)
#     tree[n2].child.append(n1)
# queue = deque([1])
# while len(queue) != 0:
#     front = queue.popleft()
#     if tree[front].child==[]:
#         continue
#     else:
#         for ch in tree[front].child:
#             if ch != tree[front].parent:
#                 tree[ch].parent = front
#                 queue.append(ch)
# for i in range(2, n+1):
#     print(tree[i].parent)






















# # 아래와 같이 큐로 작성하면 최대 O(N^2)
# import sys
# from collections import deque

# input = sys.stdin.readline

# n = int(input())
# q = deque([])

# parent = [0] * (n+1)
# parent[1] = 1

# for _ in range(n-1):
#     a, b = map(int, input().rstrip().split())
#     q.append((a,b))

# while q:
#     a, b = q.popleft()
#     if parent[a] != 0:
#         parent[b] = a
#     else:
#         if parent[b] != 0:
#             parent[a] = b
#         else:
#             q.append((a,b))

# for i in range(2,n+1):
#     print(parent[i])