primes = [2]

for n in range(3,10**6+1):
    prime = True
    for p in primes:
        if n % p == 0:
            prime = False
            break
        if p**2 > n:
            prime = True
            break
    if prime:
        primes.append(n)
print(primes)

while True:
    K,L = map(int, input().split())
    if K == 0 and L == 0:
        break
    for p in primes:
        if p > L:
            print("GOOD")
            break
        if K%p == 0:
            print("BAD",p)
            break