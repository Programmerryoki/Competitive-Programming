def main():
    MOD = 10**9 + 7

    N = int(input())
    A = [int(i) for i in input().split()]
    # dp[i][j][k]
    # i = A_i
    # j = Is the operator +?
    # k = 0 => number of equation that reach there
    # k = 1 => total sum of those equations
    dp = [[[0]*2 for j in range(2)] for i in range(N)]
    # dp[0][0][0] = 1
    dp[0][1][0] = 1
    dp[0][1][1] = A[0]
    for i in range(1,N):
        ai = A[i]
        dif = ai * dp[i-1][1][0]
        if dif >= MOD:
            dif %= MOD
        elif dif <= -MOD:
            dif = -(-dif % MOD)
        dp[i][1][1] += dp[i-1][1][1] + dif

        dif = ai * dp[i-1][0][0]
        if dif >= MOD:
            dif %= MOD
        elif dif <= -MOD:
            dif = -(-dif % MOD)
        dp[i][1][1] += dp[i-1][0][1] + dif
        dp[i][1][0] = (dp[i][1][0] + dp[i-1][1][0] + dp[i-1][0][0]) % MOD

        dif = ai * dp[i-1][1][0]
        if dif >= MOD:
            dif %= MOD
        elif dif <= -MOD:
            dif = -(-dif % MOD)
        dp[i][0][1] += dp[i-1][1][1] - dif
        dp[i][0][0] = (dp[i][0][0] + dp[i-1][1][0]) % MOD

    print((dp[-1][1][1] + dp[-1][0][1]) % MOD)

if __name__ == '__main__':
    main()