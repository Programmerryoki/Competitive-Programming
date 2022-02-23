N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
s = [[j,i] for i,j in enumerate(A)]
s.sort()
candy = [K // N]*N
K %= N
for i,j in s[:K]:
    candy[j] += 1
print("\n".join(str(i) for i in candy))