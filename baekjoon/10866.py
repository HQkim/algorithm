# 백준 10866번 덱

import sys
from collections import deque


def operation_deque(double_ended_queue, commands):
    cmd = commands[0]
    if cmd == "push_front":
        double_ended_queue.appendleft(int(commands[1]))
    elif cmd == "push_back":
        double_ended_queue.append(int(commands[1]))
    elif cmd == "pop_front":
        if not(double_ended_queue):
            print(-1)
        else:
            print(double_ended_queue.popleft())
    elif cmd == "pop_back":
        if not(double_ended_queue):
            print(-1)
        else:
            print(double_ended_queue.pop())
    elif cmd == "size":
        print(len(double_ended_queue))
    elif cmd == "empty":
        if not(double_ended_queue):
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if not(double_ended_queue):
            print(-1)
        else:
            print(double_ended_queue[0])
    else:
        if not(double_ended_queue):
            print(-1)
        else:
            print(double_ended_queue[-1])
    return double_ended_queue


def main():
    input = sys.stdin.readline
    N = int(input())
    double_ended_queue = deque([])
    for _ in range(N):
        commands = input().strip().split()
        double_ended_queue = operation_deque(double_ended_queue, commands)


main()
# 2021.06.09
