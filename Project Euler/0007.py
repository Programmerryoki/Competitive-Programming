primes = [2]
n = 3
while len(primes) < 10001:
    for p in primes:
        if n%p==0:
            break
    else:
        primes.append(n)
    n += 2
print(primes[-1])