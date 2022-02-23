N, K = [int(i) for i in input().split()]
if K >= N:
    print(N + 1)
else:
    cur = 1
    # print(N, K)
    while K < N:
        cur += K//2
        N = (N//K)*(K - K//2) + max(0, N%K - K//2)
        # print(cur,N,K)
    cur += N
    print(cur)