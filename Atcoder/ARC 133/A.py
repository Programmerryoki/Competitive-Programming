N = int(input())
A = [int(i) for i in input().split()]
m = [i for i in A if i != A[-1]]
for i in range(1,N):
    if A[i-1] > A[i]:
        tmp = [j for j in A if j != A[i-1]]
        m = min(m, tmp)
        break
print(" ".join(str(i) for i in m))