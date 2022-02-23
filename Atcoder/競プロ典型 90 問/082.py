MOD = 10**9 + 7

def modinv(N):
    num = [N%MOD]
    n = bin(MOD - 2)[2:][::-1]
    for i in range(len(n)-1):
        num.append(num[-1]**2 % MOD)
    ans = 1
    for i in range(len(n)):
        if n[i] == "1":
            ans *= num[i]
            ans %= MOD
    return ans

def sup(N):
    return int(N * (N+1))

L,R = [int(i) for i in input().split()]
total = 0
low = L-1
md2 = modinv(2)
for i in range(len(str(L)), len(str(R))+1):
    nxt = min(int("9"*i), R)
    total += ((sup(nxt) - sup(low)) * md2 % MOD) * i
    total %= MOD
    low = nxt
print(total)
# print(len(str(L)), len(str(R)))