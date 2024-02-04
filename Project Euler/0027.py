pl = 10**7
primes = [1]*pl
primes[0] = 0
primes[1] = 0
for i in range(pl):
    if not primes[i]:
        continue
    for j in range(i*2, pl, i):
        primes[j] = 0
print('primes done')
def formula(a,b):
    f = lambda n: n**2 + a*n + b
    n = 0
    while True:
        if f(n) < 0 or not primes[f(n)]:
            break
        n += 1
    return n+1 if primes[f(n)] else n

ml = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = formula(a,b)
        # print(a,b,n)
        if n > ml:
            ml = n
            print(a,b,a*b)