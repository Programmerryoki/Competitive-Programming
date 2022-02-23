from math import factorial

N, K = [int(i) for i in input().split()]
t = 0
nf = factorial(N+1)
for i in range(K, N+2):
    t += nf / factorial(i) / factorial(N+1-i)
print(t)