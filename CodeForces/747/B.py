MOD = 10**9+7

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    num = bin(k)[2:][::-1]
    mul = 1
    ans = 0
    for i in range(len(num)):
        if num[i] == "1":
            ans += mul
            ans %= MOD
        mul *= n
        mul %= MOD
    print(ans)