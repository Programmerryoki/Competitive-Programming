N = int(input())
V = [int(i) for i in input().split()]
sv = sum(V)
dp = [0]*(N+1)
for i in range(1,N+1):
    dp[i] = max(dp[:i-1] + [0]) + V[i-1]
# print(dp)
print(max(dp[-1], dp[-2]))