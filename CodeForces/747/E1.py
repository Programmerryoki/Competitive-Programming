MOD = 10**9 + 7

k = int(input())
color = [4]
for i in range(k):
    color.append(color[-1]**2 % MOD)

ans = 6
for i in range(1,k):
    ans *= color[i]
    ans %= MOD
print(ans)