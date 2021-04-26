# 2667번

import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    
    if graph[x][y] == 1:
        global num
        num += 1
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
num_list = []

for i in range(n):
    for j in range(n):
        num = 0
        if dfs(i,j) == True:
            result += 1
            num_list.append(num)

num_list.sort()
print(result)
for i in num_list:
    print(i)