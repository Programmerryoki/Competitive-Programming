MOD = 998244353

H,W,K = [int(i) for i in input().split()]
hk = [1]
wk = [1]
for i in range(K):
    hk.append((hk[-1]*H)%MOD)
    wk.append((wk[-1]*W)%MOD)
x1,y1,x2,y2 = [int(i) for i in input().split()]
total = 0
for I in range(K+1):
    J = K - I
    if (I == 0 and x1 != x2) or (J == 0 and y1 != y2):
        continue
    I -= 1
    J -= 1
    if (I == -1 and x1 != x2) or (J == -1 and y1 != y2):
        continue
    if (I == 0 and x1 == x2) or (J == 0 and y1 == y2):

    else:
        total += (hk[I] * wk[J] * 2) % MOD
    print(I,J)
    total %= MOD
print(total)