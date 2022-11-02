# BOJ 13549 숨바꼭질 3

from collections import deque


N, K = map(int, input().split())
limit = 100001
visited = [0] * limit
q = deque([(N, 0)])
answer = limit

while q:
    num, d = q.popleft()

    if num == K:
        answer = d
        break
    
    if num * 2 < limit and not visited[num * 2]:
        visited[num * 2] = 1
        q.append((num * 2, d))
    if num - 1 >= 0 and not visited[num - 1]:
        visited[num - 1] = 1
        q.append((num -1, d + 1))
    if num + 1 < limit and not visited[num + 1]:
        visited[num + 1] = 1
        q.append((num + 1, d + 1))

print(answer)