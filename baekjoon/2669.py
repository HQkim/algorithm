# 백준 2669 직사각형 네개의 합집합의 면적 구하기


graph = [[0]*100 for _ in range(100)]

for _ in range(4):
    bottom_left_x, bottom_left_y, top_right_x, top_right_y = map(
        int, input().split())

    for i in range(bottom_left_x, top_right_x):
        for j in range(bottom_left_y, top_right_y):
            graph[i][j] = 1

answer = 0
for i in range(100):
    answer += sum(graph[i])

print(answer)
