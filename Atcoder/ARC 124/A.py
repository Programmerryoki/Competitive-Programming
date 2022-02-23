MOD = 998244353

N,K = [int(i) for i in input().split()]
cum_sum = [0] * (N+1)
used = set()
for i in range(K):
    c,k = input().split()
    k = int(k)
    if c == "L":
        if k+1 < N+1:
            cum_sum[k+1] += 1
    else:
        cum_sum[0] += 1
        cum_sum[k] -= 1
    used.add(k-1)
# print(cum_sum, used)
for i in range(len(cum_sum)-1):
    cum_sum[i+1] += cum_sum[i]
# print(cum_sum)
ans = 1
for i,v in enumerate(cum_sum[1:]):
    ans *= v if i not in used else 1
    ans %= MOD
print(ans)