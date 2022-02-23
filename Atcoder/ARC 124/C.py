from math import gcd

def factor(N):
    fac = []
    for i in range(1,round(N**0.5) + 1):
        if N%i!=0:
            continue
        fac.append(i)
        if N // i != i:
            fac.append(N//i)
    return sorted(fac)

def lcm(a,b):
    return (a * b) // gcd(a,b)

N = int(input())
ab = [[int(i) for i in input().split()] for j in range(N)]
faca = factor(ab[0][0])
facb = factor(ab[0][1])
amax = 0
for i in range(len(faca)):
    for j in range(len(facb)):
        X,Y = faca[i], facb[j]
        for i in range(N):
            a,b = ab[i]
            if a%X == 0 and b%Y == 0:
                continue
            elif a%Y==0 and b%X == 0:
                continue
            break
        else:
            amax = max(amax, lcm(X,Y))
print(amax)