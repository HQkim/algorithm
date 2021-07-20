# 1946번

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arry = []
    n = int(input())
    answer = 1

    for i in range(n):
        score = tuple(map(int, input().rstrip().split()))
        arry.append(score)

    arry.sort()

    min_score = arry[0][1]

    for i in range(1, n):
        if arry[i][1] < min_score:
            min_score = arry[i][1]
            answer += 1

    sys.stdout.write(str(answer)+"\n")
