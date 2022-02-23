N,K = [int(i) for i in input().split()]
if N&1:
    if 0 < K < N+1:
        if K == (N+1)//2:
            print(N - 1)
        else:
            print(N - 2)
    else:
        print(0)
else:
    if 0 < K < N+1:
        print(N - 2)
    else:
        print(0)