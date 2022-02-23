N,K = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
dp = [float("inf")]*N
dp[0] = 0
for i in range(N):
    for j in range(1,K+1):
        if i+j >= N:
            break
        n = dp[i]+abs(h[i]-h[i+j])
        if n < dp[i+j]:
            dp[i+j] = n
print(dp[-1])