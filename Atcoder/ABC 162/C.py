from math import gcd

K = int(input())
t = 0
for a in range(1,K+1):
    for b in range(a,K+1):
        for c in range(b,K+1):
            if a == b == c:
                t += a
            elif a == b:
                t += gcd(a,c)*3
            elif b == c:
                t += gcd(a,c)*3
            elif a == c:
                t += gcd(a,b)*3
            else:
                t += gcd(gcd(a,b), c) * 6
print(t)