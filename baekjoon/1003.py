n = int(input())
for _ in range(n):
    m = int(input())
    dp = [[0, 0] for _ in range(m+1)]
    if m >= 0: 
        dp[0] = [1, 0]
    if m >= 1:
        dp[1] = [0, 1]
    
    for i in range(2, m+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(*dp[-1])
