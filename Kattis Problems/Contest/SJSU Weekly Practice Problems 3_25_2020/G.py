import bisect
primes = [2]
for n in range(3,1001,2):
    for i in primes:
        if n%i==0:
            break
    else:
        primes.append(n)

T = int(input())
for _ in range(T):
    n, e = [int(i) for i in input().split()]
    for a in primes:
        if n%a==0:
            if n//a in primes:
                p = a
                q = n//a
                break

    tn = (p-1) * (q-1)
    d = 1
    while (d * e) % tn != 1:
        d += 1
    print(d)