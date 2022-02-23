N,K = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
ind = N - K + 1
ans = [0] * (N-K+1)
rem = set()
for i in range(N-1, K-2, -1):
    ans[i - K + 1] = ind
    if P[i] >= ind:
        ind -= 1
        while ind in rem:
            ind -= 1
    else:
        rem.add(P[i])
print("\n".join(str(i) for i in ans))