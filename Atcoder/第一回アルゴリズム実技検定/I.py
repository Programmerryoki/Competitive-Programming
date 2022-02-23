N,M = [int(i) for i in input().split()]
item = [input().split() for j in range(M)]
dp = [float("inf")]*(2**N)
dp[0] = 0
for i in range(M):
    new = [float("inf")]*(2**N)
    t = int("".join("1" if k == "Y" else "0" for k in item[i][0]), 2)
    for j in range(2**N):
        p = j | t
        print(p, j, t, item[i])
        if j - p >= 0:
            new[j] = min(dp[j], new[j - p] + int(item[i][1]))
        else:
            new[j] = dp[j]
        print(new)
    dp = new
    print(dp)
print(dp[-1])