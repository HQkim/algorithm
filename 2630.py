# 백준 2630번

# Input
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

# 재귀


def split(graph):
    global white
    global blue
    n = len(graph)

    # 원소가 하나일 경우
    if n == 1:
        if graph[0] == 0:
            white += 1
        else:
            blue += 1
        return

    # 모두 같은지 체크
    total = 0
    for i in range(n):
        for j in range(n):
            total += graph[i][j]

    if total == 0:
        white += 1
        return
    elif total == n*n:
        blue += 1
        return

    # 재귀 부분
    n_2 = n // 2
    if n_2 == 1:
        split([graph[0][0]])
        split([graph[0][1]])
        split([graph[1][0]])
        split([graph[1][1]])
    else:
        split([row[:n_2] for row in graph[:n_2]])
        split([row[:n_2] for row in graph[n_2:]])
        split([row[n_2:] for row in graph[:n_2]])
        split([row[n_2:] for row in graph[n_2:]])


split(graph)
print(white)
print(blue)
