N,M = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]
n = [0]*(M)
for l in L:
    if 0 < l <= M:
        n[l-1] += 1
for i in range(M):
    print(i+1,n[i])