H,W,N,K = [int(i) for i in input().split()]
# print((H*W)%(N))
if (H*W) % (N) == (K%N):
    print("YES")
else:
    print("NO")