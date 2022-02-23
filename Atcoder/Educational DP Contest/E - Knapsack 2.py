N,W = [int(i) for i in input().split()]
items = [[int(i) for i in input().split()] for j in range(N)]
# minimum weight to achieve value x
width = 10**3 * N + 1
dp = [[float("inf")]*width for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
    w,v = items[i]
    for j in range(width-1):
        if dp[i][j] != float("inf"):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][j+v] = min(dp[i][j]+w, dp[i+1][j+v])
ans = 0
for i in range(width):
    if dp[-1][i] <= W:
        ans = i
print(ans)



# N,W = map(int, input().split())
# weight = [[int(i) for i in input().split()] for j in range(N)]
# tv = sum([i[1] for i in weight])
# dp = [[float("inf")]*(tv+1) for i in range(N+1)]
# dp[0][0] = 0
# for i in range(1,N+1):
#     we,val = weight[i-1]
#     for j in range(tv+1):
#         if j < val:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = min(dp[i-1][j], dp[i-1][j-val] + we)
# i = tv
# dpl = dp[-1]
# while 0 < i:
#     if dpl[i] <= W:
#         print(i)
#         exit()
#     i -= 1

# N,W = [int(i) for i in input().split()]
# wv = [[int(i) for i in input().split()] for j in range(N)]
# tv = sum([i[1] for i in wv])
# dp = [[0]*(tv+1) for i in range(N+1)]
# for i in range(1,N+1):
#     for j in range(1,tv+1):
#         if j > wv[i-1][1]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][1]] + wv[i-1][0])
#         else:
#             dp[i][j] = dp[i-1][j]
# i = 0
# while i < tv + 1 and dp[-1][i] < W:
#     i+=1
# if dp[-1][i] == W:
#     print(i-1)
# else:
#     print(i-2)