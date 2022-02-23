while True:
    try:
        k,n = map(int, input().split())
    except:
        break

    dp = [[1]*(k+1)] + [[0]*(k+1) for i in range(n-1)]
    for i in range(1,n):
        for j in range(k+1):
            dp[i][j] = sum(dp[i-1][max(0, j-1):min(j+2, k+1)])
    total = (k+1)**n
    ds = sum(dp[-1])
    # print(total, ds, ds / total * 100)
    print(ds / total * 100)