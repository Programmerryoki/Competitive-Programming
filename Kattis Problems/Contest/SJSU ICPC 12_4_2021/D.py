from bisect import bisect_left
from collections import defaultdict
from sys import stdin

primes = [2]
for n in range(3, int((10**6))+1):
    for p in primes:
        if n%p==0:
            break
    else:
        primes.append(n)
print(len(primes))

def factor(n):
    f = defaultdict(int)
    for p in primes:
        while n%p==0:
            n //= p
            f[p] += 1
        if n < p:
            break
    if n != 1:
        f[n] += 1
    return f

input = stdin.readline
P,R = [int(i) for i in input().split()]
planets = []
for _ in range(P):
    r,o = [float(i) for i in input().split()]
    planets.append([r, factor(int(o))])
planets.sort()
for _ in range(R):
    A,B = [float(i) for i in input().split()]
    inda = bisect_left(planets, [A, {}])
    indb = bisect_left(planets, [B, {}])
    r = [planets[i][1] for i in range(inda, indb)]
    if not r:
        print(1)
        continue
    lcm = defaultdict(int)
    for i in r:
        for k in i:
            lcm[k] = max(lcm[k], i[k])
    ans = 1
    for k in lcm:
        ans *= k**lcm[k]
    print(ans)