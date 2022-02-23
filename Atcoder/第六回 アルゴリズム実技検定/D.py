from itertools import accumulate

N,K = map(int, input().split())
A = [int(i) for i in input().split()]
aa = [0]+list(accumulate(A))
ans = [0]*(N-K+1)
for x in range(N-K+1):
    ans[x] = aa[x+K] - aa[x]
print("\n".join(map(str, ans)))