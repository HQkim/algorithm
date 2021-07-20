n, m = map(int, input().split())
graph = [input() for _ in range(n)]

count_list = []
for i in range(n-7):
    for j in range(m-7):
        count_w = 0
        count_b = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0 and l % 2 == 0 and graph[i+k][j+l] == "B":
                    count_w += 1
                if k % 2 == 0 and l % 2 == 1 and graph[i+k][j+l] == "W":
                    count_w += 1
                if k % 2 == 1 and l % 2 == 0 and graph[i+k][j+l] == "W":
                    count_w += 1
                if k % 2 == 1 and l % 2 == 1 and graph[i+k][j+l] == "B":
                    count_w += 1

                if k % 2 == 0 and l % 2 == 0 and graph[i+k][j+l] == "W":
                    count_b += 1
                if k % 2 == 0 and l % 2 == 1 and graph[i+k][j+l] == "B":
                    count_b += 1
                if k % 2 == 1 and l % 2 == 0 and graph[i+k][j+l] == "B":
                    count_b += 1
                if k % 2 == 1 and l % 2 == 1 and graph[i+k][j+l] == "W":
                    count_b += 1
        count_list.append(count_w)
        count_list.append(count_b)

print(min(count_list))
