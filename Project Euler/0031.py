cur = [200,100,50,20,10,5,2,1]
dp = [1] + [0]*200
for c in cur:
    for i in range(len(dp)):
        if not dp[i]:
            continue
        if c + i < len(dp):
            dp[c+i] += dp[i]
    print(dp)
print(dp[-1])