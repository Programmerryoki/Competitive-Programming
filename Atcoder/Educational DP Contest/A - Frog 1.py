N = int(input())
h = [int(i) for i in input().split()]
dp = [0]*(N)
dp[1] = abs(h[0] - h[1])
for i in range(0,N-2):
    dp[i+2] = min(dp[i]+abs(h[i] - h[i+2]), dp[i+1]+abs(h[i+1] - h[i+2]))
print(dp[-1])