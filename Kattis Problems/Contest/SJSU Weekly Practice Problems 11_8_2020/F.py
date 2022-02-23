N,K = map(int, input().split())
ft = [0]*(N+1)
bit = [0]*(N+1)
ans = []
for _ in range(K):
    q, *rest = input().split()
    if q == "F":
        n = int(rest[0])
        bit[n] ^= 1
        b = 1 if bit[n] else -1
        while n <= N:
            ft[n] += b
            n += n & -n
    else:
        l,r = map(int, rest)
        s = 0
        while r > 0:
            s += ft[r]
            r -= r & -r
        l -= 1
        while l > 0:
            s -= ft[l]
            l -= l & -l
        ans.append(s)
print(*ans, sep="\n")