N = int(input())
A = 1
for i in range(1,N+1):
    A = (A*i)%(10**9+7)
print(A)