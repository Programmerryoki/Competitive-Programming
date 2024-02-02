# 5984 480 17907120

def mul(a,b):
    c = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    return c

primes = [2]
for n in range(3, 10**5, 2):
    for p in primes:
        if n%p==0:
            break
    else:
        primes.append(n)
print('primes done')
diff = 2
num = 1
mn = 0
while True:
    t = num
    d = []
    for i in range(len(primes)):
        p = primes[i]
        if p > t:
            break
        d.append(0)
        while t%p==0:
            d[i] += 1
            t //= p
    d = [i+1 for i in d if i]
    m = [1]
    for i in range(len(d)):
        m = mul(m, [1]*d[i])
    ndiv = sum(m)
    if ndiv >= 500:
        print(num)
        break
    if ndiv > mn:
        mn = ndiv
        print(diff-1,ndiv, num)
    num += diff
    diff += 1