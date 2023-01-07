prime = [1]*(3*10**6)
prime[0] = 0; prime[1] = 0
primes = []
for n in range(2, len(prime)):
    if prime[n] == 0:
        continue
    for i in range(2*n, len(prime), n):
        prime[i] = 0
    primes.append(n)

T = int(input())
for _ in range(T):
    N = int(input())
    ans = None
    for p in primes:
        if N%p==0:
            if N%(p**2) == 0:
                ans = [p, N//p**2]
            else:
                ans = [int((N//p)**0.5), p]
            break
    print(f"{ans[0]} {ans[1]}")