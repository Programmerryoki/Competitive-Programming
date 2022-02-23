N = int(input())
A = [int(i) for i in input().split()]
print(sum(A))
ab = [int(bin(i)[3:],2) for i in A]
print(ab,sum(ab))
t = 0
for a in range(0,len(A)-1):
    for b in range(a+1,len(A)):
        t += A[a]^A[b]
mod = 10**9+7
print(t%mod)