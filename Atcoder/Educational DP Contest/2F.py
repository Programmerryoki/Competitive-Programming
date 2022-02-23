s = input()
t = input()
width = len(t)
height = len(s)
dp = [[0]*(width+1) for i in range(height+1)]
for i in range(1,height+1):
    for j in range(1,width+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j])
for i in dp:
    print(i)