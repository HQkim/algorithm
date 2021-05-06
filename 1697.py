# 1697번 숨바꼭질
from collections import deque

n, k = map(int, input().split())

answer = [0] * 100001
q = deque([n])

while q:
    x = q.popleft()
    new = answer[x] + 1
    t = [x+1, x-1, 2*x]
    for nx in t:
        if nx >= 0 and nx <= 100000 and answer[nx] == 0 and nx != n:
            answer[nx] = new
            q.append(nx)
print(answer[k])

# 어떻게 짤지 고민하다가 질문하기에 있는 코드를 이해하는 쪽으로 했다.
