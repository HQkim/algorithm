# boj 1764 듣보잡

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

d_listen = set()
d_see = set()

for _ in range(N):
    d_listen.add(input().rstrip())

for _ in range(M):
    d_see.add(input().rstrip())

d_listen_see = sorted(list(d_listen & d_see))

print(len(d_listen_see))
for d in d_listen_see:
    print(d)
