N,K = [int(i) for i in input().split()]
print(1 + (max(0, N - K) + (K-2))//(K-1))