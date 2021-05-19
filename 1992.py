# 1992번 쿼드트리
import sys


def solution(n, graph):

    answer = ""

    def zipimage(n, graph, answer):
        n_2 = n // 2

        if n == 1:
            return answer + graph[0][0]

        sameFlag = True
        previousBit = graph[0][0]
        for i in range(n):
            for j in range(n):
                if graph[i][j] != previousBit:
                    sameFlag = False
                    break

        if sameFlag == True:
            return answer + graph[0][0]

        q1 = [row[:n_2] for row in graph[:n_2]]
        q2 = [row[n_2:] for row in graph[:n_2]]
        q3 = [row[:n_2] for row in graph[n_2:]]
        q4 = [row[n_2:] for row in graph[n_2:]]

        answer += "("
        if sameFlag == False and n_2 != 1:
            answer = zipimage(n_2, q1, answer)
            answer = zipimage(n_2, q2, answer)
            answer = zipimage(n_2, q3, answer)
            answer = zipimage(n_2, q4, answer)
        if sameFlag == False and n_2 == 1:
            answer = zipimage(n_2, graph[0][0], answer)
            answer = zipimage(n_2, graph[0][1], answer)
            answer = zipimage(n_2, graph[1][0], answer)
            answer = zipimage(n_2, graph[1][1], answer)
        answer += ")"

        return answer

    answer = zipimage(n, graph, "")

    return answer


def main():
    input = sys.stdin.readline
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        line = input()
        for j in range(n):
            graph[i][j] = line[j]
    answer = solution(n, graph)
    print(answer)


main()
