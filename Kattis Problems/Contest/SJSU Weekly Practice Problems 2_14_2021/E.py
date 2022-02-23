P = int(input())
for _ in range(P):
    K,S = map(int, input().split())
    dp = [[[0,0], [0,0]] for i in range(S+1)]
    for i in range(1,S+1):
        dpl = dp[i-1]
        sl = sum(dpl[0])
        sr = sum(dpl[1])
        if sl == sr:
            dp[i][0][0] += dpl[0][0] + 1
            dp[i][0][1] += dpl[0][1]
            dp[i][1][0] += dpl[1][0]
            dp[i][1][1] += dpl[1][1]
        else:
            dp[i][0][0] += dpl[0][0]
            dp[i][0][1] += dpl[0][1]
            dp[i][1][0] += dpl[1][0] + 1
            dp[i][1][1] += dpl[1][1]
        if i == 1:
            continue
        dpl = dp[i-2]
        sl = sum(dpl[0])
        sr = sum(dpl[1])
        if sl == sr:
            dp[i][0][0] += dpl[0][0]
            dp[i][0][1] += dpl[0][1] + 1
            dp[i][1][0] += dpl[1][0]
            dp[i][1][1] += dpl[1][1]
        else:
            dp[i][0][0] += dpl[0][0]
            dp[i][0][1] += dpl[0][1]
            dp[i][1][0] += dpl[1][0]
            dp[i][1][1] += dpl[1][1] + 1
    print(dp[-1])