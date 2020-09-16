import sys

N = int(input())
a = [i for i in map(int, sys.stdin.readline().split())]
print(min(a), max(a))


# N = int(input())
# a = [i for i in map(int, input().split())]
# print(min(a), max(a))
