N,A,X,Y = [int(i) for i in input().split()]
total = min(N, A) * X + max(0, N-A) * Y
print(total)