MOD = 10**9 + 7

S = input()
word = "chokudai"
dp = [[1]*(len(S)+1)]+[[0]*(len(S)+1) for i in range(8)]
for i in range(1, 9):
    for j in range(1, len(S)+1):
        dp[i][j] = dp[i][j-1]
        if S[j-1] == word[i-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= MOD
print(dp[-1][-1])