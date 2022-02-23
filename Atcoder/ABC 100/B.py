D,N = [int(i) for i in input().split()]
print(N*100**D if N != 100 else (N+1)*100**D)