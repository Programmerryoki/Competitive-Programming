A,B,C,K = [int(i) for i in input().split()]
if K <= A:
    print(K)
elif K <= A + B:
    print(A)
elif K <= A + B + C:
    print(A - (K - A - B))