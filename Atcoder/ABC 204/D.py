N = int(input())
T = [int(i) for i in input().split()]
st = sum(T)
dp = [[0]*(st+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(st+1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            dp[i][j+T[i-1]] = 1
# for i in dp:
#     print(i)

for i in range(-(-st//2), st+1):
    if dp[-1][i] == 1:
        print(i)
        exit()
print(-1)