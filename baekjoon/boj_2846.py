# boj 2846 오르막길

N = int(input())
Pi = list(map(int, input().rstrip().split()))

max_height = 0
height = 0
for i in range(1, len(Pi)):
    if Pi[i] > Pi[i-1]:     
        height += Pi[i] - Pi[i-1]
    else:                  
        height = 0
    max_height = max(max_height, height)

print(max_height)
    