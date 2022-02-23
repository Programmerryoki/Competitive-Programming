MOD = 10**9+7

N = int(input())
A = [0]+[int(i) for i in input().split()]
A.sort()
ans = 1
for i in range(N):
    ans *= (A[i+1]-A[i]+1)
    ans %= MOD
print(ans % MOD)