t = int(input())
for _ in range(t):
    n,l,r = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1)