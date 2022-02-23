from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
ca = list(Counter(A).items())
total = 0
for i in range(len(ca)-1):
    for j in range(i,len(ca)):
        vi,ni = ca[i]
        vj,nj = ca[j]
        total += (ni*nj)*(vi-vj)**2
print(total)