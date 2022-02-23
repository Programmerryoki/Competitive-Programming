N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
dp = [[float("inf"),-float("inf")] for i in range(K+1)]
dp[0] = [1,1]
for i in range(1,N+1):
    new = [[float("inf"),-float("inf")] for k in range(K+1)]
    for j in range(min(i+1, K+1)):
        if j == 0:
            new[j][0] = dp[j][0]
            new[j][1] = dp[j][1]
        else:
            new[j][0] = min(dp[j][0], dp[j-1][0]*A[i-1], dp[j-1][1]*A[i-1])
            new[j][1] = max(dp[j][1], dp[j-1][0]*A[i-1], dp[j-1][1]*A[i-1])
    dp = new
    # print(dp)
print(max(dp[-1])%(10**9+7))