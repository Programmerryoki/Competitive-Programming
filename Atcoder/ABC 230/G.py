from math import gcd

lim = 450

N = int(input())
P = [int(i) for i in input().split()]
fp = {}
ans = 0
for i in range(1, N+1):
    p = P[i-1]
    if p>1 and i>1:
        ans += 1
    for j in fp:
        if gcd(i,j)<=1:
            continue
        for n in fp[j]:
            if gcd(p, n)>1:
                ans += 1
            # ans += fp[j] if gcd(i,j)>1 else 0
    for f in range(2, int(p**0.5)+1):
        if p%f==0:
            break
    else:
        f = p
    if f not in fp:
        fp[f] = []
    fp[f].append(p)
    print(fp)
print(ans)