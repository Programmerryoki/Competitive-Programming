from itertools import combinations_with_replacement

A,B,K = map(int, input().split())
print(bin(K)[2:])
for per in combinations_with_replacement([i for i in range(A+1)], B):
    print(per)