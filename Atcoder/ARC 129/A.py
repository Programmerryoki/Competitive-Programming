N,L,R = [int(i) for i in input().split()]
bn = bin(N)[2:]
print(bn)
print(len(bn))
print(bn.count("1"))
print(2**bn.count("1"))
# dp[index][bn[index] is "1"?][has this number been smaller than bn?]
dp = [[[0,0],[0,0]] for i in range(len(bn)+1)]
dp[0][0][1] = 1
for i in range(len(bn)):
    if bn[i] == "1":
        dp[i+1][0][0] = sum(dp[i][0]) + sum(dp[i][1])
        dp[i+1][0][1] = 0
        dp[i+1][1][0] = dp[i][0][0] + dp[i][1][0]
        dp[i+1][1][1] = 1
    else:
        dp[i+1][0][0] = dp[i][0][0] + dp[i][1][0]
        dp[i+1][0][1] = 1
        dp[i+1][1][0] = dp[i][0][0] + dp[i][1][0]
        dp[i+1][1][1] = 0
for i in dp:
    print(i)