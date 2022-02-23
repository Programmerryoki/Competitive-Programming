K,N,F = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(max(-1, K*N - sum(A)))