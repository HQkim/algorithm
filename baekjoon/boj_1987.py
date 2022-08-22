# BOJ 1987 알파벳

import sys


input = sys.stdin.readline
R, C = map(int, input().split())
graph = [input().rstrip() for _ in range(R)]

visited = [['']*C for _ in range(R)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_cnt = 0
stack = [(0, 0, 1, graph[0][0])]

while stack:
    x, y, cnt, word = stack.pop()
    if cnt > max_cnt:
        max_cnt = cnt
    
    if cnt == 26:
        break
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in word:
            temp = word + graph[nx][ny]
            if temp != visited[nx][ny]:
                visited[nx][ny] = temp
                stack.append((nx, ny, cnt+1, temp))

print(max_cnt)

# - dfs로 풀었는데, 처음에 pyrhon3로 제출하니 시간초과나서 pypy3로 제출하니 메모리 초과가 났다
#     - sys.setrecursionlimit(10**6)을 빼주니깐 메모리 초과가 안난다.. 아 하긴 재귀 depth가 26을 못넘으니 안넣는게 맞긴하다. 근데 sys.setrecursionlimit을 하는것 만으로도 메모리가 늘어나나?
#     - [https://velog.io/@yoopark/about-setrecursionlimit](https://velog.io/@yoopark/about-setrecursionlimit) 여기를 보니 sys.setrecursionlimit 설정만으로도 스택 메모리를 잡아 놓는 것이기 때문에 바로 메모리 초과가 나는 것이였다!..
# - 재귀로 풀 때 set나 dict로 하니깐 시간초과가 났다. 결국 `ord`를 사용해서 리스트 인덱스 접근으로 했어야 했다. set나 dict나 삽입/삭제가 시간복잡도가 O(1)이라고 알고 있는데 같은 O(1)이여도 속도가 다른가보다
# - pypy3로 제출한 코드들 중에 dfs를 스택과 set로 푸는 방식이 있었는데 그건 200-300ms로 매우 빨랐다.. 이따가 한번 봐야겠다

# 결국 방문처리를 지나온 경로로 해줘야 해주어서 가지치기를 해줘야 했다! (10번째 줄)