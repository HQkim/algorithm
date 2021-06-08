import sys

input = sys.stdin.readline

word_a = input().strip()
word_b = input().strip()

length_a = len(word_a)
length_b = len(word_b)

dp = [[0] * (length_b + 1) for _ in range(length_a + 1)]

for i in range(1, length_a + 1):
    for j in range(1, length_b + 1):
        if word_a[i-1] == word_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
