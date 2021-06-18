# 백준 2206번 벽 부수고 이동하기

import sys


def input_graph():
    input = sys.stdin.readline
    row, column = map(int, input().rstrip().split())
    graph = [[int(i) for i in input().rstrip()] for _ in range(row)]
    return (row, column, graph)

def main():
    row, column, graph = input_graph()
    print(graph)

main()