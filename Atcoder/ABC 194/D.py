N = int(input())
dp = [0]*N
dp[0] = 1
for _ in range(100):
    new = [0]*N
    for i in range(N):
