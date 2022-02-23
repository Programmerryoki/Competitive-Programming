def main():
    N = int(input())
    X,Y = [int(i) for i in input().split()]
    # dp[num of takoyaki][num of taiyaki]
    dp = [[float("inf")]*(Y+1) for i in range(X+1)]
    dp[0][0] = 0
    for _ in range(N):
        A,B = [int(i) for i in input().split()]
        ndp = [[float("inf")]*(Y+1) for i in range(X+1)]
        for i in range(X+1):
            for j in range(Y+1):
                if dp[i][j] == float("inf"):
                    continue
                ndp[i][j] = min(ndp[i][j], dp[i][j])
                if i+A <= X and j+B <= Y:
                    ndp[i+A][j+B] = min(ndp[i+A][j+B], dp[i][j]+1)
                elif i+A <= X:
                    ndp[i+A][-1] = min(ndp[i+A][-1], dp[i][j]+1)
                elif j+B <= Y:
                    ndp[-1][j+B] = min(ndp[-1][j+B], dp[i][j]+1)
                else:
                    ndp[-1][-1] = min(ndp[-1][-1], dp[i][j]+1)
        dp = ndp
    print(dp[-1][-1] if dp[-1][-1] != float("inf") else -1)

if __name__ == '__main__':
    main()