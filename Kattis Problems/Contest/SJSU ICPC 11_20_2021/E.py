from functools import reduce
from math import gcd

def eea(a, n):
    x = 1; y = 0
    x1 = 0; y1 = 1; a1 = a; b1 = n
    while b1:
        q = a1 // b1
        x,x1 = x1, x - q*x1
        y,y1 = y1, y-q*y1
        a1,b1 = b1, a1 - q*b1
    return x/a1, y/a1

T = int(input())
for _ in range(T):
    a,n,b,m = [int(i) for i in input().split()]
    K = n*m
    As = [a,b]
    ns = [n,m]
    N = reduce(lambda x,y: x*y, ns)
    zs = []
    ys = []
    for ni in ns:
        ys.append(N // ni)
        # print(pow(ys[-1],-1,ni), eea(ys[-1], ni))
        g = gcd(ys[-1], ni)
        t1, t2 = ys[-1]/g, ni/g
        zs.append(g*eea(t1, t2)[0])
    print(int(sum([As[i]*zs[i]*ys[i] for i in range(len(As))])) % K, K)