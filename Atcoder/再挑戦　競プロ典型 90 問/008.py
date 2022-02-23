N = int(input())
S = input()
MOD = 10**9 + 7

pos = [[] for i in range(26)]
for i,s in enumerate(S):
    pos[ord(s) - ord("a")].append(i)

word = "atcoder"
dp = [[0]*(N+1) for i in range(len(word) + 1)]
dp[0] = [1] * (N+1)
for i in range(1,len(word)+1):
    for j in range(1,N+1):
        if word[i-1] == S[j-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD
print(dp[-1][-1])