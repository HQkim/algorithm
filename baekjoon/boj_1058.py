# boj 1058 친구
import sys

input = sys.stdin.readline
N = int(input())
connections = [input().rstrip() for _ in range(N)]
max_friend = 0

for i in range(N):                          # 모든 사람에 대해
    friend_list = [0] * N                   # 나의 친구인 사람 리스트
    for j in range(N):
        if connections[i][j] == 'Y':                        # 나와 친구라면
            friend_list[j] = 1
            for k in range(N):
                if connections[j][k] == "Y" and i != k:     # 친구의 친구이면서 나 자신이 아니면
                    friend_list[k] = 1
    
    max_friend = max(max_friend, sum(friend_list))

print(max_friend)

        