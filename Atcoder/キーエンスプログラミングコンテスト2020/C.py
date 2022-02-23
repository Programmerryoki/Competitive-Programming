n, k, s = [int(i) for i in input().split()]
ans = [s]*k
if s != 10**9:
    ans += [s+1]*(n-k)
else:
    ans += [1]*(n-k)
print(" ".join(map(str, ans)))