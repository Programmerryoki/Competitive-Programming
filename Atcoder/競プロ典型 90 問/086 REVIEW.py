MOD = 10**9 + 7

N,Q = [int(i) for i in input().split()]
constrain = [[int(i) for i in input().split()] for j in range(Q)]
w = [0]*Q

def bit():
    ways = 0
    for i in range(1 << N):
        bit = [0]*15
        for j in range(N):
            bit[j+1] = (i // (1 << j)) % 2
        flag = True
        for j in range(Q):
            X,Y,Z,W = constrain[j]
            if bit[X] | bit[Y] | bit[Z] != w[j]:
                flag = False
        if flag:
            ways += 1
    return ways

ans = 1
for i in range(60):
    w = [0]*Q
    for j in range(Q):
        X,Y,Z,W = constrain[j]
        w[j] = (W // (1 << i)) % 2
    ret = bit()
    ans *= ret
    ans %= MOD
print(ans)