N,K = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
dp = [0]*(N)
dp[1] = abs(h[0] - h[1])
for i in range(0,N-2):
    dp[i+2] = min([dp[i+2-j]+abs(h[i+2-j]-h[i+2]) for j in range(1,min(K+1, i+3))])
print(dp[-1])