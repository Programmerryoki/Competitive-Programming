letters = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
dp = [[0]*(len(letters)+1) for i in range(len(alpha)+1)]
for i in range(1,len(alpha)+1):
    for j in range(1,len(letters)+1):
        if alpha[i-1] == letters[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# for i in dp:
#     print(i)
print(26 - dp[-1][-1])