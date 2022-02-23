ans = []
while True:
    n, m, q = [int(i) for i in input().split()]
    if n == 0 and m == 0 and q == 0:
        break
    dp = [[float("inf")] * n for _ in range(n)]
    for _ in range(m):
        u, v, w = [int(i) for i in input().split()]
        dp[u][v] = min(dp[u][v], w)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    # for i in dp:
    #     print(i)
    # print()
    t = []
    for _ in range(q):
        u, v = [int(i) for i in input().split()]
        t.append(dp[u][v] if dp[u][v] != float("inf") else "Impossible")
    ans.append("\n".join(map(str, t)))
print("\n\n".join(ans))
