A,B = [int(i) for i in input().split()]
f = lambda n, k: int(50*n + ((500*n) // (8 + 2*k)))
print(f(A,B))