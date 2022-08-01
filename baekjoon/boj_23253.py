# BOJ 23253 자료구조는 정말 최고야
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

is_possible = True
for i in range(M):
    k = int(input())
    arr = list(map(int, input().split()))
    
    for j in range(1, k):
        if arr[j] > arr[j-1]:
            is_possible = False
            break
    
    if is_possible == False:
        break

answer = "Yes" if is_possible else "No"
print(answer)