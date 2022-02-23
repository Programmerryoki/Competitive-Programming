N, M = [int(i) for i in input().split()]
A = [int(i)-1 for i in input().split()]
C = [i for i in range(1,N+1)]
for a in A:
    C = [C[a]] + C[:a] + C[a+1:]
print(C[0])