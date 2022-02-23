n, *a = [int(i) for i in input().split()]
a = a[::-1]
C = [0]*(n+1)
poly = lambda x: [x[0]] + [x[i] + x[i+1] for i in range(len(x)-1)] + [x[-1]]
P = lambda x,a: sum([a[i]*(x**i) for i in range(len(a))])
C[0] = P(0,a)
t = [1,1]
for i in range(1,len(C)):
    C[i] = P(i,a) - sum([t[j]*C[j] for j in range(len(t)-1)])
    t = poly(t)
print(" ".join(map(str, C)))