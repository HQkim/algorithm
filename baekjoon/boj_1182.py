# BOJ 1182 부분수열의 합

def dfs(depth, now):
    global count
    if depth == N:
        if now == S:
            count += 1
        return

    dfs(depth+1, now-arr[depth])
    dfs(depth+1, now)

    return 

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*N
total = sum(arr)
count = 0

dfs(0, total)

if S == 0:
    count -= 1

print(count)

