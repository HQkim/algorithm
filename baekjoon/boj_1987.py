# BOJ 1987 알파벳

import sys

input = sys.stdin.readline

def dfs(x, y, d):
    global max_d
    max_d = max(max_d, d)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not check[ord(graph[nx][ny])-65]:
            check[ord(graph[nx][ny])-65] = 1
            dfs(nx, ny, d+1)       
            check[ord(graph[nx][ny])-65] = 0
    

R, C = map(int, input().split())
graph = [input().rstrip() for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

max_d = 0
check = [0]*26
check[ord(graph[0][0])-65] = 1
dfs(0, 0, 1)

print(max_d)

# - dfs로 풀었는데, 처음에 pyrhon3로 제출하니 시간초과나서 pypy3로 제출하니 메모리 초과가 났다
#     - sys.setrecursionlimit(10**6)을 빼주니깐 메모리 초과가 안난다.. 아 하긴 재귀 depth가 26을 못넘으니 안넣는게 맞긴하다. 근데 sys.setrecursionlimit을 하는것 만으로도 메모리가 늘어나나?
#     - [https://velog.io/@yoopark/about-setrecursionlimit](https://velog.io/@yoopark/about-setrecursionlimit) 여기를 보니 sys.setrecursionlimit 설정만으로도 스택 메모리를 잡아 놓는 것이기 때문에 바로 메모리 초과가 나는 것이였다!..
# - 재귀로 풀 때 set나 dict로 하니깐 시간초과가 났다. 결국 `ord`를 사용해서 리스트 인덱스 접근으로 했어야 했다. set나 dict나 삽입/삭제가 시간복잡도가 O(1)이라고 알고 있는데 같은 O(1)이여도 속도가 다른가보다
# - pypy3로 제출한 코드들 중에 dfs를 스택과 set로 푸는 방식이 있었는데 그건 200-300ms로 매우 빨랐다.. 이따가 한번 봐야겠다