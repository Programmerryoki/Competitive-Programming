N = int(input())
dp = [[0]*3 for i in range(N+1)]
for i in range(1,N+1):
    a,b,c = map(int, input().split())
    dpp = dp[i-1]
    da = max(dpp[1], dpp[2]) + a
    db = max(dpp[0], dpp[2]) + b
    dc = max(dpp[0], dpp[1]) + c
    dp[i] = [da,db,dc]
print(max(dp[-1]))