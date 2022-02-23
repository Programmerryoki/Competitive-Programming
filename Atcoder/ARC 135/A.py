MOD = 998244353

X = int(input())
if X == 1:
    print(1)
    exit()
memo = {}

def dfs(n):
    if n == 2:
        return [1,0,0]
    if n == 3:
        return [0,1,0]
    if n == 4:
        return [0,0,1]
    if n not in memo:
        s = [i for i in dfs(n//2)]
        a = dfs(-(-n//2))
        for i in range(len(s)):
            s[i] += a[i]
        memo[n] = s
    return memo[n]

tmp = dfs(X)
ans = 1
for i in range(3):
    m = i+2
    n = tmp[i]
    bn = bin(n)[2:][::-1]
    ms = [m]
    for i in range(len(bn)):
        ms.append(ms[-1]**2 % MOD)
    for i in range(len(bn)):
        if bn[i] == "1":
            ans *= ms[i]
            ans %= MOD
print(ans)